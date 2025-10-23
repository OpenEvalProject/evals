# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75720.sa0](https://doi.org/10.7554/eLife.75720.sa0)

Using extensive molecular dynamics simulations with a novel enhanced sampling technique, the authors are able to characterize the structural flexibility of the SARS-CoV2 spike protein and identify new conformational states. These insights will be valuable to the design of novel strategies that modulate the interactions of the spike protein during the infection process.


---

# Peer review - Round 1

Editors:
- Qiang Cui, https://ror.org/05qwgg493 Boston University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75720.sa1](https://doi.org/10.7554/eLife.75720.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "The Inherent Flexibility of Receptor Binding Domains in SARS-CoV-2 Spike Protein" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Volker Dötsch as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) More thorough discussion of the conformational transition pathways, including key intermediates and their structural stability.

2) More quantitative analysis of the key structural states identified in the study, evaluation of their potential accuracy, especially the intermediate states for which limited high-resolution information is available from experiments so far.

3) Considering the publication of several recent computational analyses of the same system, it would be important to further highlight the unique insights from the current analysis.

Reviewer #1:

Understanding the conformational dynamics of the spike protein of SARS-CoV-2 can provide valuable guidance to the design of new antivirial drugs and vaccines. Previous computational studies employed either bias or enhanced sampling along specific structural variables, leading to incomplete understanding in the structural flexibility and conformational transition mechanisms. In this study, the authors take advantage of a newly developed enhanced sampling method (gREST_SSCR), which does not specify any biasing coordinates, to better characterize the structural ensemble of the spike protein. The results therefore complement previous simulations studies and enhance our understanding in the conformational flexibility and transition mechanism of the spike protein. For example, the simulations identified intermediate states that were observed in smFRET experiments but not in higher-resolution cryo-EM studies. The sampled conformational ensembles also revealed cryptic binding sites that potentially bind to drug molecules and binding interfaces of antibodies. The results will be instructive to the design of new approaches for battling this important pandemic.

While I find the simulations impressive and analyses rather comprehensive, I hope the authors would consider the following questions.

1. For comparing with the cryo-EM structures in Figure 2 – can the comparison be made more quantitative?

2. On the criterion for selecting the "solute" residues – it is understandable that charged residues at domain interfaces might be good choices since interactions involving them are likely to be reorganized during large-scale conformational transitions. Nevertheless, it will be useful to elaborate how the specific set of residues are chosen. For example, are they involved in different salt-bridge interactions in different conformational states identified in the cryo-EM structures?

3. Considering recent publications that also highlighted conformational flexibility of the spike protein, roles of glycan in modulating conformational flexibility/transition and binding interface with other proteins, and cryptic binding sites of small molecules, it would be important to clearly highlight how observations from the current work differ from these complementary computational efforts.

Reviewer #2:

In the manuscript by Sugita and colleagues, the authors describe the results of extensive simulations of the spike protein of SARS-CoV-2. They used generalized replica exchange with solute tempering of selected surface charged residues (gREST_SSCR) to study the conformational changes of the SARS-CoV-2 spike (S) protein, specifically the up and down motion of the receptor binding domains (RBDs). They observed the Down, one-Up, one-Open and two-Up-like structures in their simulations, and compared them with the cryo-EM structures. The solvent accessible surface area (SASA) of the RBD was measured at each of the above states to study the effect of different conformations for ACE2 and antibodies binding. They further used k-means clustering and re-clustering to obtain five main conformation ensembles, providing structural insight to a previous smFRET experiment and, more importantly, the transition pathway from the Down to one-Up state. The pathway was characterized by the analysis of contacts and hydrogen bonds. At the end, the authors applied P2Rank to search for the formation of druggable pockets in the intermediate structures.

Overall I found the simulation and analysis methods used in this study very impressive and the findings are important. However, I found the Results section of the manuscript to be rather confusing, making it difficult to capture the major findings of the studies until I read the Discussion section.

1) The definitions of the many different spike conformations throughout the manuscript were the most confusing part for me. The first four structures (D_sym, 1U, 1U_o, and 2U_L) are the most well defined, with their hingeA and hingeB value provided and a clear figure (Figure 2) showing their 3D structures as well as where they located in the PC space and Hinge angle space. However, things start getting murkier when it comes to the 5 ensembles (Down_sym, Down_like, Int2, Int3 and 1Up) found by k-means clustering. It was not discussed in the main text whether Down_sym is the same state as the D_sym state defined before, or how Down_like is different. It is also not clear what Int2 and Int3 states look like. Only a careful reader would find there are actually more than 5 clusters and their cluster centers can be interpreted from Figure 4—figure supplement 1, and they are grouped into 5 major conformations under the scheme from Figure 4—figure supplement 4e, and their respective distributions on the Hinge angle space was plotted at Figure 4—figure supplement 5. It is not helping that the authors go on referencing these minor clusters in the main text (one-Up-like, 1U_L and 1U_a in the main text, IUa, 2Ua_L, 2Ub_L in Figure 5) without providing their definitions. I believe such information is crucial for the reader to understand the second half of the manuscript, and I suggest the authors reorganize the figures to make the information clear and easy to access.

2) The second point I want to make goes hand-in-hand with the first point. I find the transition paths and the intermediate states to be the most interesting and novel findings of this work, yet the discussions on these findings are very brief in the manuscript. How does the hinge and twist angles change when you go from one state to another? What are the roles of the intermediate states (Int2 and Int3) in this opening of the RBD? I noticed in Figure 4—figure supplement 5(b) there is no arrow pointing from state I3b to 1U_L. Is I3b a trap state? How did the authors come to this conclusion? How does I3a differ from I3b? What about the one-Open state that the authors suggest to be important for binding? The discussion on the 1Up-to-2Up transition is equally brief. I believe these questions deserve a much longer discussion than a brief page-and-a-half skim over.

Reviewer #3:

This article focuses on the varied conformations that the SARS-CoV-2 spike protein takes and how this relates to the function of this protein and potential for drug targets. Extensive molecular simulations at the atomistic level were performed to provide details of the structural transitions of the spike protein and its protective sugar shield. Overall, this manuscript is a strong study on the spike structural states and transitions using enhanced molecular dynamics. This work clearly lays out details of transitions near the down and up states and how glycans can stabilize or alter conformational states and transitions. This work adds important details to the growing body of literature on the spike protein.

The main weakness in this work is the focus on intermediate structures in drug binding. Although this is an interesting idea, the details of the stability of the intermediate states are not described. Stability is key to stable for drug binding to deactivate the spike protein. It is unclear without more detail if these intermediate states are likely to be stable for drug binding and deactivation.

Author Recommendations (details):

1. Lack of details for intermediate states: I don't see analysis showing intermediate stability of I2a and I3a. How stable are these and where are they on the reduced free energy surface in Figure 1? Short-lived intermediates are not good targets for drugs. Figure 4 provides some details in the structure but no info on the free energy surface near the intermediates is provided and how this relates to stability.

2. Accuracy of intermediate state: How do you know these are accurate intermediate states? Any experimental comparison that would suggest these exist?

3. Is spike a good drug target?: The spike protein is certainly an important target for antibodies and vaccines. However, it may not be the best target toward drugs and a current FDA approved drug focuses on another part of the virus action. Some discussion on why the spike protein is believed to be a good target should be included in the manuscript.

4. Supporting figure format: I find it difficult to read and follow the format for the supporting figures that are tied to a main figure and not in a single pdf document. I would hope that eLife allows a single supporting document with all the figures numbered to easily review like all other journals.

5. Add omicron: With the current state of SARS-CoV-2, the list of mutants/variants in the intro should now include omicron.
