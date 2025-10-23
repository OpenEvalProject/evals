# Peer review - Round 1

Editors:
- Karsten Kruse, https://ror.org/01swzsf04 University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79862.sa0](https://doi.org/10.7554/eLife.79862.sa0)

This theoretical investigation provides important findings on the role of active mechanical feedback on tissue remodelling. The authors present convincing evidence that mechanically enforced myosin recruitment at cell-cell junctions can lead to tissue expansion in the direction perpendicular to an externally applied uniaxial mechanical stress. The relevance of the proposed mechanism for convergence–extension systems requires more investigation through comparison with experimental data.


---

# Peer review - Round 1

Editors:
- Karsten Kruse, https://ror.org/01swzsf04 University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79862.sa1](https://doi.org/10.7554/eLife.79862.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Generating active T1 transitions through mechanochemical feedback" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Improve the comparison with experiments (see reports).

2) Argue more convincingly for biological relevance.

3) Put the positive feedback tension/myosin more into context and discuss possible effects of mechanisms that are an alternative to the one you implemented (see reports).

Reviewer #1 (Recommendations for the authors):

This paper presents a numerical study of tissue convergent extension during epithelial morphogenesis. It builds upon several earlier works, including so-called vertex models, and single junction mechanical models. The specificity of the model presented lies in its active component: a positive feedback exists between Myosin activity and mechanical tension in each junction. This leads to interesting tissue-scale dynamics. Upon tissue pulling, the authors report conditions for which intercalation occurs perpendicular to the pulling direction. They provide a rather detailed analysis of the model and its numerical outcome, and a qualitative comparison with convergent extension in avian embryos.

Strengths:

The model is presented in a rigorous manner and with a lot of details and pedagogy. It is discussed in comparison with other models of the field, and the similarities and differences are clearly and honestly presented by the authors in their discussion.

The numerical study provides interesting and possibly counter-intuitive predictions in which tissue convergent extension can occur perpendicular to an external pulling axis, due to a positive feedback between myosin motors recruitment and tension which leads to the formation of Myosin chains (or cables) along the pulling axis.

The conditions in which this regime of tissue remodeling can occur (under the hypotheses of the model) are thoroughly investigated. Finally the authors go a bit beyond the sole numerical study, and analyze experimental data of the polarized tissue flow occurring upon primitive streak formation in avians.

Weaknesses:

Although the numerical investigation is thorough and the model hypotheses are clearly stated, the paper falls a bit short of convincing readers that the emergent behaviors observed in the model are of actual biological relevance.

The hypotheses and ingredients of the model are clearly stated (1) junctions are viscoelastic, (2) junctions are active, i.e. they can generate tension through myosin, and (3) positive feedback between tension and myosin. Yet the 3rd hypothesis, which gives its singularity to the model, is not discussed enough, and its relevance to well-known convergent extension systems is not analyzed. In the paper, the positive feedback arises from the decrease of unbinding rate upon tension increase. This "catch bond" hypothesis (note: the term catch-bond only appears once, in the methods) is at the core of all the results obtained in the paper, and this should be clearly stated and discussed. As for the positive feedback, one could also imagine that it is not the unbinding rate that decreases upon tension increase, but rather the myosin recruitment rate that increases. Would that be formally equivalent? The authors should address this point and its biological implications.

The comparison between the model outcome (notably, the T1 transitions preferably oriented in the direction perpendicular to pulling) and existing experimental data is a bit elusive. The authors propose a semi-quantitative comparison with convergent-extension occurring upon primitive streak formation in avians. The data and conclusion is not fully convincing, partly because of the polarization data itself (Figure 8C), and partly because it's not clear what would be the equivalent of the external pulling force in this self-polarizing flow.

The authors also mention the germband of Drosophila, but the model is, I believe, not relevant for that system. Although there is indeed an external force pulling the tissue (pulling posterior midgut), polarization is perpendicular and extension parallel to the pulling force (the opposite of the model outcome).

In that spirit, they should also discuss pulling experiments (fly wing disc / Mao lab, suspended epithelia / Charras lab) where it's not so clear that topological transitions occur upon pulling.

Finally, the paper builds upon already existing models of junction and tissue mechanics. Beyond the vertex model itself, the hypothesis of a feedback between myosin activity and tension has also been around in the field for some time, including in modeling papers (which authors acknowledge honestly).

In conclusion:

The paper presents a thorough numerical analysis of T1s and convergent extension upon tissue pulling when a positive feedback exists between Myosin and junction tension. Yet, the fact that this type of model and hypotheses are not completely new, combined to a lack of comparison to experimental data (except for avian gastrulation) makes it a bit difficult for the reader to assess the novelty of the findings presented in the paper.

I liked the presentation of the model a lot, the details given, the pedagogy, the comparison with what already existed (Discussion section), and the thorough analysis of the model outcome.

On the other hand, I find it a bit difficult to see whether the novelty is strong enough for publication in eLife:

First, because somewhat similar models exist in the field. According to the authors, the specificity here is the inclusion of the positive feedback for the active part of the model. Yet, other models that the authors cite include a similar type of feedback, although they might not specifically focus on topological transitions and convergent extension. In addition, the existence of such a feedback (and its possible consequences on tissue morphogenesis) has been around in the field for a while, under various forms (here, the authors chose a catch-bond type dissociation rate for myosin).

Second, because the comparison (even qualitative) with existing experimental data remains elusive.

Hence the major finding of this paper is that a tissue in which a positive feedback between tension and motor recruitment exists can display active intercalations and convergent extension perpendicular to an external pulling force. In which experimental systems this prediction could be relevant remains to be determined.

– Does the positive feedback tension/myosin need to stem from the catch bond model? Could one imagine increased motor recruitment open junction/cell stretch (This would be in line with some experimental data, including stretching experiments). Would that be formally equivalent to the catch bond, or would that change the outcome of the model? If yes, how?

– In which systems do people observe tissue extension along the direction perpendicular to pulling? The authors only refer to the avian embryo in which the nature of the flow (embryo-scale) makes it a bit difficult (at least for me) to interpret what is the chicken and what is the egg. A lot of data is now available out there for analysis. It would be great to see the same kind of analyses in other experimental systems. Notably, the fly germband (that the authors rapidly mention) seems to behave completely differently, with cables of Myosin perpendicular to the pulling axis (pulling force being exerted by the posterior midgut). How about convergent extension in the zebrafish or Xenopus embryos?

– What happens at the boundaries? Here we look at a central patch of cells. And somewhat related question, how would that work in a closed geometry (such as the fly embryo). I feel that the avian discussion (paragraph 1 of discussion) could be expanded with considerations on how the feedback can produce long range flows even though only a small patch of cells is initially "activated".

– Authors should cite Duda et al. (Dev Cell 2019) from the Mao group. In this article it is shown that Myosin polarizes and form cables upon external tissue stretch in the fly wing disc. This is fully relevant to their model and it is somewhat surprising that they do not cite it. Disclaimer: I'm not on that paper

– The authors present their model as "one of the simplest descriptions" that features the three main ingredients required (viscoelastic junctions, active junctions, positive feedback myosin/tension). What would be the simplest and why didn't they choose it?

– Authors should better explain the rationale of the "elastic barrier" term B(l-a) , as compared to the k(l-l0) term.

Reviewer #2 (Recommendations for the authors):

Sknepnek et al. study a model for junction dynamics in a two-dimensional vertex model, intended to describe epithelial mechanics. In the model, a concentration of myosin on each half-junction evolves according to a chemical balance equation and induces an active tension in the junction. The chemical balance equation incorporates a mechanical feedback, whereby myosin unbinding is inhibited at high tension. The authors first study a single junction and consider thresholds for the junction to fully contract. They then investigate the behaviour of a few « active » junctions in a passive network and a fully active vertex model. They find that at intermediate external pulling force and myosin-induced tension, the simulated epithelium can undergo convergence-extension against the pulling force.

The manuscript describes a work which is seriously and rigorously performed. The simulations are analysed thoroughly with a serious quantification effort. The authors have made an important effort of clarity in their study.

My central question is about the motivation of the manuscript. The central theme of the manuscript authors study « contrarian » active T1 transitions which induce convergence extension in the direction orthogonal to an externally applied stress. I would disagree with the authors that this is the only type of active T1 transition. For instance polarised transitions which are oriented by the epithelium chemical polarity and induce converge-extension in the absence of external tension, as is thought to be the case during germ-band elongation, could also be called « active ». From the manuscript it is not clear to me why inducing convergence extension as a response to external tension, against the external tension, is important or biologically relevant. I think the authors should significantly clarify the rationale for their study.

In that respect I am not sure that the comparison with experiment is very useful. My understanding is that essentially myosin cables in the chick embryos appear oriented along the direction of tissue contraction, which seems to make sense if these cables are actively contracting. I am not sure that this observation strongly supports the much more detailed model proposed by the authors; notably the notion that myosin polarises in response to external tension.

Judging from Figure 6, the authors also observe relatively limited convergence extension happening against the external force. I wonder if this may be due to myosin molecules playing both the role of the force-exerting molecule and the sensor in the model? For instance, possibly if a secondary molecule responding to external tension, and itself inducing myosin polarisation, a more permanent convergence-extension could be induced?

– I think the authors may have overlooked the reference « active instability and nonlinear dynamics of cell-cell junctions », Krajnc, et al, PRL, 2021. The approach and questions seem very close to the current manuscript. I think the results and approach of this study should be contrasted to the current work.

– When comparing Figure 7C and Figure 6, I had the impression that Figure 7C showed significant « negative » convergence extension for large values of β (0.75), why the authors say that this is not the case in the caption of Figure 6?

– The model assumes a constant number of available myosin molecules in each cell. It was not clear to me if this assumption is important for the results of the model?

– I do not understand the reason for the factor « z » in the second term of the right-hand side of Equation 5.

Reviewer #3 (Recommendations for the authors):

The authors propose a mechanism for the dynamics of cell-cell junctions under an applied external mechanical load. In their theoretical analysis they assume that myosin recruitment and therefore active contractile stress in a junction increases with an applied external load. They find that this mechanism can induce a T1 transition through which adjacent cells exchange neighbours such that an originally aligned junction is reorientated perpendicularly to an applied uniaxial extensile stress. By using a generalised vertex model they also find that this effect on an isolated cell-cell junction can lead to convergence-extension of a tissue, where the extension occurs perpendicularly to the applied uniaxial extensile stress. In both cases, the phenomenon is present for a broad range of parameter values. Eventually, the authors compare their theoretical results to convergence extension of a part of a tissue in an early chick embryo.

The theoretical analysis is carried out mostly through simulations and is done in a convincing way. The dynamics assumed for a single junction is based mostly on reasonable assumptions and differs from earlier works. It appears though that the assumption of a monotonic decrease of the myosin unbinding rate with the applied force needs more justification. I would assume that for sufficiently high forces, this rate will increase as is the case for catch bonds. Taking such an effect into account might limit the range of parameter values for which stress-induced convergence-extension is observed. Also, it was unclear to me whether all ingredients of the model where necessary to obtain the observed effect. In particular, I wonder what happens if either of the dashpots or the springs are eliminated? Finally, I do not understand why m_0 should describe effects of the surrounding. Shouldn't this effect be included in T_ext? Otherwise the theoretical analysis is convincing and justifies the conclusions of the authors.

I am less convinced by the comparison with experiments on gastrulation in early-stage chick embryos. Although the relative orientation between myosin cables and the direction of extension agrees with that in the theory, I fail to see where the external uniaxial extensile stress should come from. It thus appears that an essential element of the theory is not checked for in the experiments. The authors write themselves in ll 395: "Although it is yet to be experimentally confirmed, it is plausible that the symmetry breaking event that induces the initial myosin polarity occurs as a result of anisotropic tension combined with cell differentiation early in development." The authors should clarify this point, which seems to be central to the authors' idea that mechanical signalling drives convergence-extension in this case. Otherwise, the experimental data do not add much to the work.

The authors frequently use the term "polarisation" or "polarised" when referring to the alignment of the myosin cables, for example. This notion implies directionality, for example, a difference between left and right in Figure 2, which is not present. I would suggest that the authors rather use 'anisotropy'.

The text exhibits some jumps between figures that are not always referred to in order, for example between Figures2 and 3 or Figure 4C and 4B. The authors might want to adapt their text to the figures or vice versa.

In Figure 1A the term \β m is hard to see. Please, improve.

In Figure 3 the colour code is confusing. In A black, red, blue correspond to different junction classes, in B and C to different mechanical quantities and in D again to different junction classes but not the ones in A. Please, improve.

Ll 49 "With cellular behaviours being coordinated over thousands of cells in the case of the chick embryo, biochemical signalling alone is unlikely to account for the observed motion patterns." Even though I have a guess, I do not really understand this argument. Can you add some words to explain, why the long-range coordination is at odds with pure biochemical signalling?

L 218 side a -> side OF a

L 256 along the direction the central junction -> along the direction OF the central junction

Ll 274 could you add a panel to show this?

In Figures6 and 7A, convergence-extension is not really visible assuming that the initial state was square. Maybe you can show a sequence similar to Figure 2?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Generating active T1 transitions through mechanochemical feedback" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Your model doesn't seem to apply to the fly germband elongation, in which the invaginating midgut (pulling external force) and the T1s occur along the same axis, with cables perpendicular to the pulling axis. In your response, you insist that the pulling force is rather the ventral invagination than the posterior midgut (hence a force perpendicular to tissue elongation and T1s, and parallel to the cables, as in their model). This overlooks that the germband does not extend without the posterior midgut pulling (Torso), while it does without the ventral mesoderm invagination. In the paper, claims about their finding applying to germband extension are found in the intro and discussion, without other justification. These comments should be removed unless very strongly justified, as it seems that they are based on a direct misinterpretation of previous observations.

When the germband is mentioned you usually cite a paper that does NOT deal with the germband (Jacinto et al. 2002, which is about dorsal closure). And you also cite Duda et al., even though it's a wing disc paper, in which cables form parallel to the pulling force, (as in their model, but in contrast with the germband). This could be confusing and even detrimental to your work when readers familiar with fly morphogenesis read it.
