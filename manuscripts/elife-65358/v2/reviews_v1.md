# Peer review - Round 1

Editors:
- Olivier Rivoire, College de France France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65358.sa1](https://doi.org/10.7554/eLife.65358.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper proposes a new theoretical perspective to analyze multisite modification networks based on the symmetries that they display and the way in which these symmetries can be effectively broken. This perspective has several interesting implications, including for the analysis, synthetic design and evolution of these networks.

Decision letter after peer review:

Thank you for submitting your article "Symmetry breaking meets multisite modification" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

The three Reviewers concur to find the manuscript of interest but raise concerns related to its presentation and its relation to the previous literature. They welcome a resubmission provided that it addresses the points raised by the Reviewers and in particular the following essential points:

1) A clarification of the nature of the differences between the 'cases': to what extent are they really different? wouldn't it possible to have a more synthetic and unified presentation? all reviewers pointed out the manuscript in general and Figure 1D in particular would benefit from an effort of clarification

2) Relation to previous literature: to what extent are the results different from previous proposals, in particular zero-order ultrasensitivity, sequestration effects and previous analyses of symmetry breaking in multisite modification systems? (see in particular references given by Rev #2)

3) To what extent is symmetry breaking a necessary condition for the properties that it can induce, in particular absolute concentration robustness? and to what extent does symmetry need to exactly hold?

4) Make more explicit the evolutionary scenarios that are only briefly sketches: what are the assumptions on the symmetries that are 'naturally' expected to be present prior to any evolution?

5) Include mention of symmetries in other parameters, notably dissociation constants

Reviewer #1 (Recommendations for the authors):

Post-translational modifications of proteins at multiple sites, for instance by phosphorylation, play a key role in signal transduction and processing. Their system-level behaviors, which include bistability and oscillations, can be analyzed on a case-by-case basis with mathematical tools from dynamical systems. The main contribution of the paper is to propose a new perspective that goes beyond this case-by-case approach. This is achieved by pointing out that protein networks based on multisite modifications can display symmetries and that these symmetries can be broken to give rise to properties of biological relevance: ordering, directionality, concentration robustness,…

The paper includes on one side a mathematical analysis of two-site modifications systems, with an detailed analysis of the symmetries that they may display, the conditions for these symmetries to be present, and the conditions under which they may be broken. On the other side, the paper includes an extensive general discussion of the relevance of these analyses for actual biological system.

This is not a standard paper presenting a specific result or a novel technical method but a thought-provoking proposal revisiting the dynamics of multisite modification systems from a new perspective. While it is difficult to judge it by the usual standards, it should be of broad interest. For instance, no reference is made to any particular experimental system but the authors convincingly argue for the relevance of their point of view for interpreting natural systems and designing synthetic ones.

My main comment concerns the generality of the concept of symmetry: the paper advocates it in general but focuses on simple cases of reflection symmetry with 2-site modification systems. What other symmetries, if any, may be expected and of interest? How may the approach generalize beyond 2-site modification systems? Addressing exhaustively these questions may be outside the scope of a single article, but it would be worth fleshing out a few possible extensions.

– Figure 1D is key to define what is meant by symmetry but in my opinion not sufficiently informative. In particular the symmetry in kinetic structure is highlighted while the constraints on enzymes, which seem as essential, are not represented. For instance requiring k1=k3 is not sufficient, something like k1[K1]=k3[P2] is in fact needed? Also, as represented, Case 1 and Case 2 appear as formally equivalent (related through a 45 degree rotation). I was also wondering if more transparent notations could be used for ki, aj, which would reflect the (possible) symmetries?

– Another example of information processing at the molecular level where symmetry plays a key role is the MWC model of allostery. It may be worth mentioning it as, beyond the analogy, post-translational modifications can be associated with allosteric transitions.

– The two concepts of information processing and symmetry breaking bring to mind the possibility of encoding a bit of information in the symmetric states: could it be relevant in the context of post-translational modifications?

Reviewer #2 (Recommendations for the authors):

In this paper, the authors demonstrated that the symmetry in the concentration of different phospho-forms of a protein could be broken in multisite phosphorylation processes in proteins, even if the reaction's kinetic parameters to produce those are the same. They analyzed some different classes of symmetries in the kinetics for a protein with two phosphorylation sites and showed some of those shows the pitchfork bifurcation or the Hopf bifurcation. Also, they discussed that the relevance of the symmetry breaking for the absolute concentration robustness.

The analysis of classes of networks with different symmetries may be of use for future research in the field. Also, the relationship of the symmetry breaking to the absolute concentration robustness may be interesting. However, the discussion of whether symmetry breaking is a necessary condition for the absolute concentration robustness is still lacking. Moreover, the connection to previous studies has not been argued enough. For example, the symmetry-breaking mechanism may be related to the Goldbeter-Koshland-type zero-order ultrasensitivity and the enzyme competition. However, the connection has not been discussed sufficiently. Also, the symmetry breaking in the multisite modification has been studied for networks with feedback. However, mention of those studies is still lacking.

This paper still has several problems to be addressed, as described below.

1) The writing often lacks clarity and sharpness and is poorly organized. Although the authors showed their analyses for different symmetries in order from Case 1 to 3, the central mechanism of the symmetry breaking may be almost the same in these three classes. Moreover, the ordered distributive DSB seems sufficient to demonstrate the symmetry breaking by such a central mechanism. Hence, I recommend reorganizing the paper; to state detailed analyses for the ordered distributive DSB and an intuitive explanation at first, and then discuss three classes in the following sections.

2) The authors stated that Case 1 symmetry breaking was observed "only in the common kinase, common phosphatase case," and Case 2 symmetry breaking "is broken only for different kinase and different phosphatase case." It looks strange to me. Changes of variables, e.g., from A_00 to A_01, A_11 to A_10, k_1 to k_2, k_3 to a_2, and so on, can transform one case to the other. Thus, the two cases seem to be identical. Please explain why those two cases are different.

3) The mechanism of the symmetry breaking may be a combination of the Goldbeter-Koshland-type zero-order ultrasensitivity and a competition for the enzyme among different phospho-forms of the protein. However, there is no discussion about the relationship of symmetry breaking they found to zero-order ultrasensitivity and phenomena related to the enzyme competition.

4) The authors claimed the importance of the symmetry among phosphorylation and dephosphorylation speeds. However, even if the phosphorylation and dephosphorylation speeds are the same, the difference in dissociation constants can drastically change the actual reaction speed when substrates with different modification states compete for the limited amount of enzyme. (For example, Hatakeyama and Kaneko, PLoS Comput. Biol. (2014) and Hatakeyama Kaneko, Phys. Rev. Research (2020)). Hence, I recommend that the authors emphasize the importance of the symmetry in the dissociation constant as well as the modification speed, to make a reader pay attention.

5) The author demonstrated that if the network is symmetric and the symmetry in concentration is broken, the concentration of some phospho-form of the protein shows the absolute robustness. However, they did not show whether symmetry breaking is necessary for the absolute concentration robustness. Does a network without symmetry never show the absolute concentration robustness?

6) The authors cited papers only written by Ueda's group (Ode and Ueda, (2018), Jolly et al., (2012), Sugui et al., (2017), and Shinohara et al., (2017)) about the circadian clock as references. However, the circadian clock generated by the multisite modification has long been studied in cyanobacteria. Thus, the basic concept has already been stated in previous studies. For example, a generation of the oscillation by a protein with two phosphorylation sites was published in Rust et al., "Ordered phosphorylation governs oscillation of a three-protein circadian clock." (2007). The importance of enzyme sequestration for the oscillation was published in van Zon et al., "An allosteric model of circadian KaiC phosphorylation." (2007). Also, the mechanism of temperature compensation by the competition for the enzyme was published in Hatakeyama and Kaneko, "Generic temperature compensation of biological clocks by autonomous regulation of catalyst concentration." (2012). I recommend citing those papers in addition to Ueda's paper, for the healthy development of the scientific community.

7) The symmetry breaking in the multisite modification has been studied, at least for networks with explicit feedback. Hence, it may be better to tone down the title and some claims.

Reviewer #4 (Recommendations for the authors):

In this manuscript, Ramesh and Krishnan analyze on a theoretical level symmetry breaking in multisite models of covalent modification. The basic idea is that while the underlying network dynamics may preserve certain symmetries, these symmetries can be broken leading to asymmetric states, with for example unequal levels of doubly modified or unmodified phosphoforms. The symmetry breaking requires the presence of nonlinearities which fundamentally result from sequestration effects of the necessary enzymes/substrates. Overall, I found the paper to be a highly original contribution, with some very nice results that could open up new directions, for example in understanding the evolution of asymmetric networks. Their extensive analytical and numerical work clearly supports their conclusions, and suggestions for experimental signatures of broken symmetry are given. This work may have consequences for the fields of network evolution and synthetic biology.

In general, I found the manuscript to be well-written. Nevertheless, the paper is definitely not an easy read, despite clearly significant efforts from the authors due to the complexity of the subject matter.

One aspect that needs further attention is to what extent the system needs to be exactly symmetric to exhibit the behavior studied by the authors. This is an important point as some of the required symmetries are not natural: for example, in Case 1 of Figure 1D, k_1=k_3 which means that a phosphorylation and a dephosphorylation reaction must be precisely balanced. There is some effort towards analyzing this in Figure S5, but I think this aspect needs to be given much greater prominence and discussion also in the main text.

The authors also argue that evolution may have started with a symmetric network with broken symmetry as a starter towards asymmetric networks. This is an interesting idea but isn't it more likely that the networks were just asymmetric to begin with (which has a much bigger parameter space), and that was subsequently exaggerated, rather than starting from an a priori fine-tuned symmetric configuration? A similar issue arises with claims that an observed asymmetric network may not have biased dynamics but may instead simply be due to symmetry breaking within a symmetric network. Without more knowledge surely the former is still much more likely?

Key to the symmetry breaking is the nonlinearity introduced by sequestration effects without the need for explicit feedback. However, I think this needs an expanded discussion (probably with some equations) in the main text rather than being relegated to the (extremely large) methods. This is a central point, I think.

I didn't find the left side of Figure 1D very helpful for my understanding. Also, the explanation of the "square" network topology wasn't made very clear; I didn't find it more straightforward than the depictions in Figure 1A-C, for example.
