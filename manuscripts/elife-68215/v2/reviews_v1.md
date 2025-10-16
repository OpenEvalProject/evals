# Peer review - Round 1

Editors:
- Felix Campelo, The Barcelona Institute of Science and Technology Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68215.sa1](https://doi.org/10.7554/eLife.68215.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper will be of interest to neuroscientists, and more broadly to scientists working on membrane fusion. A combination of experiments fusing an elegant nanodisc-cell fusion assay and of mechanical models reveals a new mechanism by which Synaptotagmin-1 mechanically promotes the opening of the fusion pore induced by SNARE proteins.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "The neuronal calcium sensor Synaptotagmin-1 and SNARE proteins cooperate to dilate fusion pores" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor.

Having considered your revision plan. our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

Two reviewers read the author response. Their comments are presented below. In brief, the reviewers and the reviewing editor understand that the additional experiments, which are necessary for revision of the experimental part of the article, could be hard to perform in the near future because of the pandemic. At the same time, the author replies to the reviewer comments on the theoretical part of the work, do not appear satisfactory.

Computational part

"In cell-attached recordings, the patch of membrane that is under study is under high tension due to adhesion to the walls of the pipette. Strong adhesion of the membrane to the walls of the glass pipette is needed to obtain a high-resistance seal (the so-called "Gigaseal") for low-noise recordings. Previous measurements show the membrane tension in the patch is ~1 pN/nm [37]. This is consistent with our model that obtained a tension of 0.66 pN nm-1 as a best-fit parameter by comparing the model-predicted slope of the free energy of pore dilation for pores of size ~ 1 nm between the model prediction and the experimental measurement when only SNAREs were present in a previous study of ours [3].

Forces that oppose membrane tension at the nanodisc boundary arise presumably from the bending rigidity of the ApoE proteins, and from their interactions with the lipids. A radially inward force per unit length equal to the membrane tension acts on the ApoE scaffold. Assuming only the bending rigidity opposes this inward force, we can compare the membrane tension to the threshold force per unit length where a circular ring buckles, kT Lp /d2 , where : and d and Lp are the radius of the cross-section of the circular ring and its persistence length respectively. As the scaffold proteins consist of a series of α-helical regions interspersed with unstructured regions [38], and a typical persistence length of α-helices is ~ 100 nm [39], the buckling threshold is ~400 pN nm-1 assuming a thickness : d~ 1 nm, much larger than the membrane tension of 0.66 pN nm-1"

The should be a misunderstanding here. According to the classical literature on the buckling instability of a ring, the radial force per unit length of the ring (the membrane tension in the present case) leading to the instability is, approximately, γ~(kT Lp)/r3 , where r is the ring radius. Taking Lp = 100nm, as suggested by the authors, and r~10"nm" , according to the dimension of nanodiscs used in the work, one gets, practically, a vanishing critical tension. This must mean that, as a result of the pore nucleation, the tension drops to zero.

This means that the model is inconsistent with the reality in this essential point.

"We agree that the toroidal shape is not an exact fusion pore solution, but we use this shape for simplicity, and we believe it captures all the important features of a more exact solution. It has the advantage that the biophysical aspects are clearly articulated. For this reason, toroidal pores have been assumed in many previous theoretical studies (e.g. [40-42])."

This is not a convincing argument. In the previous studies the toroidal pore approximation was used for the cases of two infinitely large membranes connected by a fusion pore. In the present study, the dimension of the nanodisk is of the same order of magnitude as the pore radius so that the deviation from the toroidal shape may have essential consequences for the results.

One of the consequences of the toroidal pore assumption is the conclusion that SNARE reorientation results in the expansion of the pore waist, which is one of the central conclusions of the model. An alternative outcome could be an increase of the tangent angle to the membrane profile at the ND rim without the waist expansion. A detailed computational analysis avoiding the toroidal shape assumption is needed to resolve this issue.

"Regarding the torque at the nanodisc edge, the question raised by the reviewer, it can be shown that the downward bending is small, so that the flat annulus approximation at the outer nanodisc edge does not deviate by a large amount from the exact solution. The argument is as follows. (1) The angle made by an annular piece of membrane of width : at the nanodisc edge is ? ~ @:!/A, where @ is the downward force per unit length at the nanodisc edge and A is the membrane bending modulus. (2) The net downward force is the same at any cross section of the pore. At the pore waist net downward force is ~ 2C(D + F/2)H, assuming the mean curvature of the waist *+,- is negligible. Here, D , F and H refer to the radius of the pore, the membrane thickness, and *+,- tension respectively. Thus, for pores of radii similar to the membrane thickness, the force per unit length at the ND edge is @ ~ FH/J./ where J./ is the radius of the ND. (3) This force per unit length gives an angle ? ~ FH:!/AJ./. Using : ~ 5 ->, and other values as in Table S1, we get an angle ? ~ 4. Thus, the bending of the membrane is negligible near the nanodisc"

This reasoning is very hard to follow. (i) For some reason, the expressions include the membrane thickness, while the latter is already accounted for by the bending rigidity, which is also a part of the same expressions. (ii) Further, the authors estimate the angle of 4o at the ND edge, while the question is about the curvature (mean curvature) there rather than the angle. The expression for the curvature includes the angle derivative along the contour length, not just the angle itself. (iii) Moreover, the origin of the constant downforce, used by the authors for their argumentation, is unclear. Indeed, the cell membrane is, practically, horizontally oriented so that the downforce at the bottom of the pore should vanish. (iv) The suggestion of an almost vanishing mean curvature in the pore waist is incompatible with the assumption of a considerable lateral tension.

"The protein scaffold around the nanodisc can be formed by various configurations of the apolipoprotein E variant containing the N-terminal 22 kDa fragment (ApoE422K) [38]. In all cases, it is thought that two rows of stacked α-helical segments form a belt at the boundary of the nanodisc. The α-helical segments interact laterally and are connected by short linkers [38]. The torque contribution could arise either from the twisting rigidity of the α-helices or from the interactions between the proteins and the lipid molecules.

As the reviewer says, we assumed constant torque. We found a potential quadratic in the twisting angle could not reproduce the energetics of large pores of radii ~ 3 – 6 nm when ~15 SNARE complexes are present at the fusion pore without Synaptotagmin-1 [3].

In fact, we did consider the effect of the torque for pores of smaller radii. The proteins are twisted only when the radius or the height of the pore are large enough so that the rim of the toroidal pore where it joins with the flat membranes reaches the boundary of the nanodisc. Such radii or heights are larger than the equilibrium values predicted by the model, so it costs energy to access them. Thus, such states do not contribute much to the statistical average at the equilibrium values of radius and height."

A proposal about a specific mechanism of a constant (independent of deformation) torque generation should enable quantitative estimation of this factor. Otherwise, this energy contribution appears too speculative to be published.

Experimental part

The reviewers were disappointed to learn that the authors chose not to do an additional experiment, in particular, of determining the binding kinetics of nanodiscs to the cell membranes. The reviewers believe this experiment would yield an important piece of data showing what constitutes the rate-limiting step in the fusion pore assay the authors have developed. Moreover, the technical difficulties stated in the rebuttal, mainly high fluorescence backgrounds, may be bypassed using techniques such as FRET.

However, the senior author professed difficult situations in his lab midst the current pandemic situation. Therefore, at least regarding Comment 1, the authors need to state these potential issues in their experimental assay-including low rates of fusion pore opening, low cooperativity and unawareness of the rate-limiting step-and discuss the limitations and reservations in interpreting their data sets. It may then be possible to proceed as the authors have suggested (on page 7 of the rebuttal).

Reviewer #1:

The article by Z. Wu et al. addresses experimentally and theoretically the mechanism by which Syt-1 contributes to fusion pore dilation. The system used consists of nanodiscs fused with SNARE-containing cell membranes. The new proposal of the work is that the fusion pore expansion is driven by an intra-membrane reorientation of Syt1 hydrophobic loops, which leads to rotation of SNARE complexes and the resulting increase of the inter-membrane distance. The latter leads to an increase of the fusion pore radius.

In my view the article can not be published in the present form.

The suggested mechanism of the fusion pore dilation is crucially based on the theoretical model which, in its present form, raises questions.

1. The model assumes that the whole membrane is exposed to a constant lateral tension. I am wondering whether any relevant level of tension can exist in this system given that the edge of the nano-disc is free, i.e. is not subjected to any external force. It is true that the apolipoprotein scaffold at the disc edge could sustain some tension due to the scaffold compression and bending/twisting rigidities provided that the latter are sufficiently large.

Estimations of sustainable tensions based on the feasible values of the protein scaffold rigidities are necessary to support the model.

2. It is assumed that for a substantial range of the pore radii the pore can be described by a toroidal shape. This implies that the fragment of the nano-disc membrane between the ND edge and the rim of the pore is flat. This does not seem to be feasible mechanically since it would violate the torque equilibrium at the disc edge. Indeed, the tension in the cell membrane generates a rotational moment with respect to the ND edge (the pore height serving as a lever), which must be counteracted by torque at the edge. On the other hand, the existence of the edge torque necessarily means generation of the membrane curvature next to the disc edge.

Consideration and estimation of this torque and the related shape of the ND membrane, including their dependence on the pore radius are absolutely necessary to justify the model and its major prediction on the increase of the pore radius upon increasing of the pore height. Also, in case the scaffold is too soft to develop large enough torques to equilibrate the rotational moment of the membrane tension, the whole description becomes questionable.

3. Considering the partially toroidal shapes of the pore, the authors assume the torque at ND edge to be constant since the related energy contribution is linear in the angle. I am wondering about the physical origin of such a constant torque and why its effect was not considered for smaller pore radii.

Reviewer #2:

The authors have done a remarkable job of creating an assay for the fusion pore that does not require capacitance measurements or amperometry, but detects a transient in the DC current through a cell membrane , interpreted as the fusion pore, when a nanodisc is applied to the cell surface.

I do not understand why the conductance is limited in time, and what the meaning of the time course is. If the conductance rises and then falls, does it mean that competing factors are changing in time? In that case, what does the mean pore conductance mean for this complex time course?

While this system shows an effect of Syt1, it only explains a very small part of the biological effect of Syt1. The effect of calcium on synaptic exocytosis follows a fourth-power continuously increasing curve with presynaptic [Ca2+]free, this is a large effect by 20 uM, and not in keeping with the rather modest (3 fold) increase in activity in the author's model with [Ca2+]free in an S-shaped curve that saturates rapidly. An explanation for the saturation of the Ca effect is needed.

The section, "Calcium-dependent membrane-insertion of Syt1 C2AB, but not curvature generation, is necessary for pore dilation" did not seem particularly convincing. I did not follow this explanation: "Membrane insertion of these hydrophobic residues expands the membrane in one leaflet, creating an area mismatch, which relaxes as the membrane curves away from the wedge-like insertion. This membrane buckling is thought to contribute to the triggering of release (37, 52, 53). Nor was I convinced that "Thus, membrane penetration is required for pore expansion by Syt1, but curvature generation is not." Or that " It is well known that calcium induced loop insertion causes a reorientation of the C2 domains (86, 87)."

Reviewer #3:

This manuscript by Wu et al. reports on use of in vitro assays to study opening of fusion pores catalyzed by SNAREs and syanptotagmin1 (Syt1). One of the persisting questions in Ca2+-triggered exocytosis is how these machineries catalyze fusion pore opening, which is allegedly energetically-expensive, on millisecond scales as in the case of central nerve systems.

Recent incorporation of the electrophysiology tools is a welcoming addition to the field because it makes characterization of the fusion pores more quantitative, to the extent that would be likely unattainable with other methods. The authors formed nanodiscs reconstituted with 8 copies of R-SNAREs and Syt1 each (~25 nm diameter), and expressed Q-SNARE proteins in a flipped orientation on HeLa cell membranes. Fusion events between the nanodiscs and the cell membranes led to conductance of ions through fusion pores, which was monitored via the electrophysiology tool. The authors carried out detailed and quantitative analysis on the various physical properties of fusion pores including the average conductance and fluctuation rates. The authors took one step further to introduce various mutations to the C2B domain and studied their effects on the fusion pore properties.

These observations convincingly showed that in the in vitro assay the authors developed, SNAREs and Syt1 work in a concerted manner to open fusion pores with larger diameters and increased fluctuations with Ca2+ and PI(4,5)P2 working as important cofactors. The authors propose a model where enhanced membrane penetration of the C2B domains in the presence of these cofactors tilts up the SNARE complexes. This increases height of the pore structure, which in turn leads to dilation of fusion pores.

Although these results provide some interesting insights into the molecular mechanisms underlying fusion pore opening, there are issues that need to be addressed before recommendation of this manuscript for publication in eLife.

Comment 1. One concern is the rate of fusion pore opening is still low, a few times within 10 minutes, which is orders of magnitude slower than what is observed and Ca2+-evoked exocytosis in physiological milieu. Although it would be too demanding to expect reconstitution of ms-scale Ca2+-triggered pore opening in the current work, it is still important to identify the rate-limiting step for fusion pore opening in the in vitro assay the authors have developed.

The authors may want to study of binding kinetics of the nanodiscs to cell membranes under the reaction conditions used in this study probably using single-particle fluorescence microscopy or capacity measurement. If the binding latency is only a small fraction of the observed long latency, the priming step after binding could define the rate-limiting step. This priming may involve many molecular re-arrangement between two fusing membranes, such as formation of SNARE complexes (in trans or cis forms) and inter-SNARE complex arrangement (shown in Figure 6E) and recently reported interactions between SNARE complexes and the C2B domains (Ref. 76, 77). To sum up, the authors need to characterize the binding kinetics of nanodiscs and cell membranes and specify the rate-limiting step of the current in vitro fusion pore assay in the manuscript.

In this vein, it is also important to see how the pore open frequency is modulated as a function of Ca2+ concentration, which is currently missing in Figures 4 and S5. This is because the binding between fusing membranes is known to be substantially accelerated in the presence of Ca2+.

Comment 2. In the model shown in Figure 6, the authors suggest that enhanced binding and penetration of the C2B domain mechanically tilt up the SNARE complexes, thereby catalyzing larger fusion pores. The authors further suggest that this levering action can withstand restoring force of the fusion pore up to 14-16 pN.

This estimation, however, appears to be at odds with the observations made in previous single-molecule force spectroscopy studies. For example, the single neuronal SNARE complex is stabilized by a huge free energy of 65 kBT, but even the SNARE complexes are fully unzipped upon application of 16 pN tension (Ref. 92, 93). In addition, binding between the negatively charged membranes (with 5 mol% PI(4,5)P2) and C2B already shows repetitive binding and unbinding under 3 to 4 pN tension (Ref 62). Thus, although the model proposed by the authors is interesting, it may be more realistic to expect that membrane penetration of multiple C2B domains has a moderate steering effects for the SNARE complexes lining the fusion pores, rather than working as strong mechanical supports maintaining the suggested elongated pore structure.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "The neuronal calcium sensor Synaptotagmin-1 and SNARE proteins cooperate to dilate fusion pores" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Felix Campelo as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Vivek Malhotra as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Patricia Bassereau (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

We request no additional experiments. We are only asking for some revisions that are mostly aimed at improving the clarity the manuscript as well as some extra computations regarding the model's assumptions. These additional computations should be relatively straight-forward for the authors. For these required revisions, see the detailed reports from Reviewer #1 and Reviewer #3. In particular, we'd like to emphasize on the following:

1. About the BCs used for the computations (see e.g. Eq. (8) of the SI Appendix): the authors should study (or provide a solid argumentation on why this might not be necessary) the shape and energies when the tCell membrane does not relax to a perfectly flat state but to a catenoidal shape.

2. The final section of Results presents some modeling work with C2A. There are no relevant experiments and the results are not discussed in the Discussion section. It is not clear how this section fits into this paper, so unless the authors can adapt it to provide a logical explanation in the context of this paper, this section should probably be removed.

Reviewer 1:

The calcium sensor Synaptotagmin-1 (Syt1) is known to be a key element for neuronal SNARE-mediated fusion, but how fusion proceeds is still debated and many different scenarios and physical models have been proposed. In this work, Z. Wu and collaborators use an interesting assay for measuring single fusion event with a very good time resolution (ms): v-SNARE proteins are reconstituted in large nanodiscs and fuse with "flipped cells" expressing t-SNAREs facing the extracellular media. Syt1 interacts either as a full length protein co-reconstituted in the nanodisc or as a truncated soluble version (C2A+C2B domains, or mutants) added in the patch pipette. Single fusion events are followed by electrophysiology using voltage-clamp in the cell-attached mode, as a function of PIP2 in the cell membrane or calcium in the medium. The authors focus mostly on the effect of Syt1 on pore expansion. In parallel, they have developed a mathematical model for fusion of nanodisc and cells based on Helfrich energy for the membrane fusion part and theory of elasticity for the scaffolding by ApoE around the nanodisc. The experiments clearly show that Syt1 promotes the growth of the fusion pore in a way dependent on binding to PiP2 and calcium concentration. Its interaction with SNAREs also contributes to pore expansion. The C2B+C2A domain (C2AB) is sufficient to induce this effect and Ca2+-dependent penetration of the hydrophobic loop is essential. These dependences and the pore growth rates are nicely reproduced by a model where at low calcium, the C2B domain binds to t-SNARES and to PiP2, remaining parallel to the membrane and keeping the pore small or closed. When calcium increases, the membrane insertion of the hydrophobic loop while being connected to SNAREs produces a tilt of about 15{degree sign} of the SNARE-Syt1 complex. SNARE-Syt1 acts as a mechanical lever on the pore edge, which changes the pore shape and tends to open it more. The C2A domain's loop strongly boosts the kinetics of the opening process. Altogether, the lever model accounts well for the experiments presented in the study, in contrast with different models previously published.

With this work, we can expect conceptual advances on the contribution of Syt1 to neuronal membrane fusion. In addition, the modelling of the mechanical deformation of a nanodisc and of its scaffold in the presence of a pore should be more generally relevant to experiments involving mechanosensitive membrane proteins or other pore forming structures.

I was not a reviewer in the initial version of the manuscript, but I have now read carefully both the current revised manuscript and the rebuttal letter including the detailed responses to the reviewers of the previous submission.

In general, I think that this manuscript deals with an interesting topic (fusion pore expansion by Syt and SNARES) using a variety of tools (experimental study of pore size and dynamics using nanodisks, as well as detailed modeling of the pore shape).

Regarding the experimental part, and following the discussion from the previous submission, although I agree that the ND binding kinetic measurements would have been an important piece to be added, I accept the statements made by the authors in this revised manuscript.

Regarding the modeling part, I do appreciate the effort made by the authors in implementing and solving the shape of the pore without the toroidal pore assumption. The finding that the tension required to open up the pore is different in the exact solution as compared to the toroidal pore is interesting and important. It also helps the authors discuss why they think that the scaffold is not buckling as a response to tension (and bending) of the ND membrane.

That being said, I have some specific comments about the model, and about some of the assumptions made there:

1. Perhaps to me the most important one is the BCs shown in Eq. (8) of the SI Appendix. There the authors assume that the membrane (on the tCell side) is flat (phi(L)=0) at a certain distance (Rinf=30nm) from the pore axis. A couple of thoughts.

– Rinf is chosen somehow arbitrarily.

– Why does the membrane need to relax to a flat state far away from the pore and not a catenoidal geometry (which also has zero bending energy)? This latter condition could be implemented by assuming phi(L)≠0. To me, intuitively (so maths might proof me wrong of course), such a geometry could make that zipping does not lead to pore expansion but maybe to a change in the catenoidal angle? I think that the authors should discuss if this makes sense or not.

2. I've noticed some inconsistencies in the "Mathematical Model of the ApoE scaffold" in the SI Appendix. In particular:

– some references are missing in the appendix.

– Eq. (14) in the app. please use Uscaffold and not F.

– Two AHs per ApoE scaffold are assumed to estimate Ksoft and Khard, is that correct? This should be explained and reasoned in the text as the readers are left to deduce that from the numbers.

– pg. 11 appendix: with the definition given in Eq. (14) of k=(Khard-Ksoft)/(2 RNLP2), and using the values in the text just above that, I get k=2.1 kBT/nm and not 4.2 kBT/nm as the authors wrote. Please verify. And then the evaluation of the twist angle for a 2 pN torque, in my hands, appears to be phi=7.5 degrees and not 30 degrees. If this is correct, how does it alter the results of the model?

3. What's the relative importance of the hydration energy to the overall free energy of the pore? I'm asking because the pore is assumed toroidal for Eq. (16) in the SI appendix, but the shape is not toroidal anymore. Could the authors elaborate on that?

4. Figure 1B: Is it fair to compare IF signal of PIP2 in permeabilized cells to the signal in non-permeabilized cells?

5. Figure 2A: Did the authors considered a multiple comparison test when inferring the statistical significance, or just performed one-to-one Student's t-test between the different conditions? If the answer is the latter, then caution should be taken in interpreting the observed differences (see e.g. PMID: 31596231)

Reviewer #2:

The calcium sensor Synaptotagmin-1 (Syt1) is known to be a key element for neuronal SNARE-mediated fusion, but how it proceeds is still debated and many different scenarios and physical models have been proposed. In this work, Z. Wu and collaborators use an interesting assay for measuring single fusion events with a very good time resolution (ms): v-SNARE proteins are reconstituted in large nanodiscs and fuse with "flipped cells" expressing t-SNAREs facing the extracellular media. Syt1 interacts either as a full length protein co-reconstituted in the nanodisc or as a truncated soluble version (C2A+C2B domains, or mutants) added in the patch pipette. Single fusion events are followed by electrophysiology using voltage-clamp in the cell-attached mode, as a function of PIP2 in the cell membrane or calcium in the medium. The authors focus mostly on the effect of Syt1 on pore expansion. In parallel, they have developed a mathematical model for fusion of nanodisc and cells based on Helfrich energy for the membrane fusion part and theory of elasticity for the scaffolding by ApoE around the nanodisc. The experiments clearly show that Syt1 promotes the growth of the fusion pore in a way dependent on binding to PiP2 and calcium concentration. Its interaction with SNAREs also contributes to pore expansion. The C2B+C2A domain (C2AB) is sufficient to induce this effect and Ca2+-dependent penetration of the hydrophobic loop is essential. These dependences and the pore growth rates are nicely reproduced by a model where at low calcium, the C2B domain binds to t-SNARES and to PiP2, remaining parallel to the membrane and keeping the pore small or closed. When calcium increases, the membrane insertion of the hydrophobic loop while being connected to SNAREs produces a tilt of about 15{degree sign} of the SNARE-Syt1 complex. SNARE-Syt1 acts as a mechanical lever on the pore edge, which changes the pore shape and tends to open it more. The C2A domain's loop strongly boosts the kinetics of the opening process. Altogether, the lever model accounts well for the experiments presented in the study, in contrast with different models previously published.

With this work, we can expect conceptual advances on the contribution of Syt1 to neuronal membrane fusion. But in addition, the modeling of the mechanical deformation of a nanodisc and of its scaffold in the presence of a pore should be more generally relevant to experiments involving mechanosensitive membrane proteins or other pore forming structures.

This manuscript is an extensive revision of a paper that was previously submitted to eLife. The main critics on the previous version were on the mechanical models behind the interpretation of the data, in particular on the mechanical resistance of the ND assembly to pore opening, the toroidal pore model and the torque exerted by the protein scaffold on the nanodisc periphery. It is true that these models are essential for providing a mechanism. As far as I can tell and not being a theoretician myself, I think the authors did a good job at addressing the different issues that were raised by the former editor and reviewers. These new additions reinforce their conclusions and their interpretation of their data. On the experimental side, considering the requests after the previous review and the still difficult situation related to the COVID pandemic, I consider that the new version includes the necessary discussions and precautions, in particular on the limitation of the assay to assess the binding kinetics. Personally, I think that the paper is ready for publication.

Reviewer #3:

This study by Wu et al. presents interesting new results obtained with a very sophisticated experimental system and incorporating very sophisticated modeling into their interpretations. The principal results advance the idea that synaptotagmin promotes fusion pore expansion through its interactions with membranes. The idea of a role for synaptotagmin in pore expansion has been around for quite some time but the present results extend what we know about this process. In particular, Syt1 binding to the lipid bilayer to exert force and change fusion pore shape is novel and interesting. All in all, it is a strong paper but a number of concerns require attention.

1. When the authors state ~4 copies of syt1 and VAMP2 per disc face (page 4 and 5), this is an average and the actual number will have a wide range due to inherent fluctuations when numbers are small. This variation in copy number must be incorporated into the discussion.

2. How do the authors arrive at 10 nm maximum diameter (top of P 5)? There must be a limit in a 25 nm NLP but the actual value is hard to specify, and the 10 nm value seems like a guess.

3. The authors use the Boltzmann distribution to go from the observed pore size distribution to the size dependence of pore energy. This is an impressive leap of insight and creativity. But the Boltzmann distribution applies to systems at equilibrium and the observed conductance time course is probably very far from equilibrium. The underlying process appears to be irreversible. Each pore opening episode looks like a trajectory through a complex energy landscape. Some acknowledgement of these shortcomings must be made.

4. On P 9 the authors discuss changes in pore radius, height, and shape. Doesn't that complicate the relation between diameter and conductance?

5. The last sentence of the Mathematical modeling section on P 10 states that increasing pore height increases membrane bending energy. Ref 109 shows that increasing height reduces bending energy.

6. The final section of Results presents some modeling work with C2A. There are no relevant experiments and the results are not discussed in the Discussion section. I do not see how this section fits into this paper.
