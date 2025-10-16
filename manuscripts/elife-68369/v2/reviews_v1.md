# Peer review - Round 1

Editors:
- Toby W Allen, RMIT University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68369.sa1](https://doi.org/10.7554/eLife.68369.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This article presents state-of-the-art molecular dynamics simulations of the pH-gated pentameric ion channel GLIC, which has been the subject of many structural and functional studies. GLIC can be considered as a model system for pentameric ligand-gated ion channels that are responsible for fast chemical-electrical communication between cells in animals. The findings include the solution of open- and closed-like channel forms, intermediates and a "pre-desensitised" state. The approach reproduces modulation by pH and opposing mutations, correctly reproducing loss or gain of function, representing convincing proof of the success of the approach. Overall, the sampling of channel dynamics is significant and the description of state interconversions sheds new light on pLGIC mechanisms. The reviewers were convinced by the substantial changes and additions to the manuscript, as well as the new insight into the roles of pH and mutations in GLIC function. Concerns over convergence, sampling and methods descriptions have been allayed and the manuscript is now suitable for publication.

Decision letter after peer review:

Thank you for submitting your article "Markov State Models of Proton-and Gate-Dependent Activation in a Pentameric Ligand-Gated Ion Channel" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Toby Allen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Frédéric Poitevin (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the reviewers agree on the strengths and importance of the findings, the following changes or additions are required:

1. Analyse one the numerous mutants that are blocked in the so-called locally-closed state, thereby helping the community to understand the nature of this often-encountered phenotype.

2. Demonstrate convergence and sampling, including proof of lack of dependence on the initial path.

3. Better describe of the nature of the observed states (especially the locally closed state) and the tICA gating coordinates.

4. Additional methods description and clarification is needed, with clearer relation to past simulation studies to avoid misapprehensions.

Reviewer #1 (Recommendations for the authors):

The authors state that the problem with some past methods is a presumed pathway (which should be distinguished from a presumed finite set of coordinates/collective variables, as in Ref.20). Yet the MSM is not without any assumptions. The seeding of simulations in any MSM, including here, stems from an initial presumed gating transition from some simplified model. See above comments.

In the beginning of the Results section (page 5) we see a typical representation of free energy within a tICA1/2 space. See above comment. Can the key tICA1 vector be visualised, say with a vector mapping (movements of residues…) on the structure to allow it to be more readily interpreted? Moreover, it is not clear what tIC2 represents by analysis of figure 2 and later figures, and its importance to gating not immediately obvious. Is there a physical interpretation for it? Overall, I find the discussion around figure 2 to be wanting of more physical interpretation.

The authors find predominantly closed channels, although I233T (which shifts pH50 to allow conduction even at neutral pH in experiments) revealed a second open-like free energy minimum. Protonation revealed a much broader second open minimum (though still by far predominantly closed, even at low pH). This predominant closure was not seen in in past string solutions of Lev et al., and it is not clear how this is consistent with the observed pH50 for wildtype GLIC experimentally. See above comment on this, relating to the preprint in Ref.33, which appears to be the main evidence used by the authors for a low probability of a conducting form.

Regarding other states, I feel the intermediate states (such as those of states I-V with partial TMD/ECD change) have not been well characterised, or their implications explained as well as could be. Also, the authors could better visualise the location of any LC forms on the maps and explain their roles in gating (see above comments). In figure 2 the LC states are said to lump in with closed state structures (page 6). The dots in figure 4 have no colours. I guess some of the left dots are LC? See my comments above about confusion over LC. It is particularly interesting that one state with -2' constriction may relate to the desensitised state (although the authors see no barrier towards it, and so its relation to a desensitised state is not clear). Why the method cannot sample the actual desensitised state is not well explained – though may suggest a limitation in the analysis based on microsecond trajectories.

Analysis of states against past variables (as in Lev et al., Ref 20) mostly goes as expected, although the ECD behaviour does not (page 10). Though pH dependence is seen, the MSM does not reveal clear bloom and twist diffs O-C states and the authors suggest it is an artefact of x-ray crystals. While twist was less obvious, ECD spreading did differ between states in the past model based on strings by Lev et al., Is this because the finite space of Lev et al., or becoming trapped near those values? Why did the ECD spread effect disappear in this current model? Was it present after the initial seeding but vanished in subsequent MD libraries, or did this come from the initial seeding procedure?

Symmetry of the ECD decreases in closed state, and at high pH. This is as to be expected based on the higher structural diversity (and symmetry loss) of the ECD seen in Xray of the closed/high pH structure. A lot has been made about the role of asymmetry. Can the authors better explain to the reader why asymmetry in gating really matters?

In comparison to the previous string method on page 11, the authors write that barriers like 1-1.5 and 1.5-2 are lower than 1.5 and 2.5 kcal/mol, suggesting the current model extracted lower barriers – presumably being better sampled. However, given the errors I would just say they are consistent.

The statement on page 4 that Lev et al., only used short picosecond timescale simulations in their string method could be misleading for the readers. The string method used by Lev et al., makes use of large libraries of 5 and 20ps trajectories to sample the directions of change, but are carried out in parallel and repeated for many hundreds of iterations, such that the timescale sampled is much longer than that suggested by the authors here. More critically, the string method is an enhanced sampling approach such that timescales of motions cannot be judged by these values, as they adaptively sense the directions of change, allowing the approach to explore configurational space well beyond the actual simulation times. In fact, one might suggest the MSM approach used here, based on libraries of 1 microsecond free trajectories, may be limited in the states they can explore for processes that occur on much longer timescales. While it is always possible to have more sampling of random trajectories in the string method, I would say the main advantage of the present MSM is the lack of presumption of order parameters, which could be further explored in string methods. I do note, however, that one of the conclusions here (on page 12) is that the variables used by Ref.20 were consistent with the findings here.

Regarding the methods, overall the techniques used could be better explained, both for the MD/MSM expert and the general reader, avoiding jargon and relying on packaged methods, and better justifying the choices made. Things like eBDIMS, TIC etc will not mean much to many readers in the current form. The motivations for the choices and their details are important to this study.

Reviewer #2 (Recommendations for the authors):

The authors should take the opportunity of their working methodology to explain to the community the role of the LC state: is it an on-pathway form in which some of the mutants get stuck? or is it something different (off-pathway)?

– To this effect, an in-depth study of one of the many known LC mutants is needed.

– p. 2 There is a rather bold and questionable general statement in p. 2 about experimental structures, stating that "the stability required for crystal packing or cryo-EM data processing results in structures mostly representing metastable states".

I strongly suggest replacing the word "mostly" by "sometimes".

Reviewer #3 (Recommendations for the authors):

My main recommendations to the authors are very general and do not require to be answered for acceptance of publication.

Regarding the apparent subjectivity in the clustering choices and the difficulty/impossibility of exhaustive sampling for this kind of system, it would be interesting to motivate the choices made (5 states, PCCA+, …). For example, would the authors recommend their approach for simulations involving other large systems – can it be transferred – or was it thought in reaction to the particular sampling obtained here? Elements of answers to this question have the potential to help overcome the problem of robust analysis of undersampled datasets, which could benefit greatly the simulation community.

It is somewhat unclear to me what the new insights exactly are:

– The idea that protonation is mainly a driver of compaction, not of the gating is interesting. Unfortunately, there is no discussion of the combinatorial problem that protonation poses or mention of constant pH simulations that would be more realistic than applying fixed protonation that were proposed in the past – exploring the effect of a few selected protonation state changes would be interesting to see if the results are robust to a few perturbations.

– Discussion about desensitized state is interesting; it would have been nice to hear more from the authors about their take on the possibility to access this regime with simulations. In principle MSM have the potential to yield kinetic models that could be directly compared to the ones extracted from electrophysiology; what is the authors take on this? Will that ever be possible? When? Would a more experimental approach be desirable, instead of post-hoc comparison?
