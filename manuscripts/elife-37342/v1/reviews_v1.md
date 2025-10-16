# Peer review - Round 1

Editors:
- Anna Akhmanova, Utrecht University Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.37342.031](https://doi.org/10.7554/eLife.37342.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "The role of intermolecular interactions in the gating mechanism of formins" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

The reviewers appreciated the importance of your modeling work and its potential to significantly advance the mechanistic understanding of formin activity. However, they also pointed out ambiguities in interpreting the effect of FH2-actin contacts, actin twist, and steric hindrance based on the provided data. The relation of the results of this work to prior proposed stepping mechanisms and open/close gating was not clear. The reviews also pointed out that the coarse-grained model suggests larger FH2 motions compared to the all atom simulations, and thus both models cannot be used as independent evidence for the same effect. Since it is a policy of eLife to invite revisions only when the path to successfully addressing the reviewer comments is clear and the revisions can be completed within two months, and this does not seem to be the case here, we cannot further consider the current version of your paper for publication. However, we will be prepared to consider a new submission, which would fully address the comments of all three reviewers. In case you decide to prepare such a new submission, please note that to resolve the apparent inconsistency between the two types of models currently included in the paper, one of the models could be abandoned in favor of the most accurate and relevant one.

Reviewer #1:

The authors describe several models for the interaction of the formin FH2 domain with actin filaments (all atom MD, metadynamics, coarse grained). They argue that mDia1-bound barbed ends become more accessible for polymerization and Cdc12-bound barbed ends less accessible, compared to Bni1-bound ends. Since this is the same trend as in the experimentally measured gating factors, the authors propose that their simulations provide an explanation of the origin of gating.

Demonstrating that the gating factors of formins can be calculated from first principles would indeed be a great theoretical advance worthy of a publication in eLife. It would demonstrate the power of the modeling methods that would have broad implications in the cytoskeleton field and beyond.

However, I have the following comments and concerns:

* The paper will have stronger impact if the authors provide predictions for future experiments based on their improved understanding of the system. For example mutations that could change the gating factor or predictions for the gating factors of other formins that have not yet been measured.

* This study provides many different pieces of evidence pointing towards the picture of gating factors mDia1>Bni1>Cdc12, on average. These studies are very useful given that very little is known at this level. However, because of fluctuations, need for long simulation times and differences between the models make each measure (or their combination) somewhat ambiguous. One such example is the evolution of the twist angles in Figure 4. They show a trend, which is however not completely clear due to fluctuations and lack of clear equilibration. Further, in this case the order seems to be different: mDia1>Cdc12>Bni1. I provide some further examples below.

* Figure 3 demonstrates the volume fraction in two different FH2 configurations at the barbed end that should differ by a step of one FH2 member forward or backward. Presumably only one of the two is the main conformation prior to polymerization of a new actin subunit. I understand there are no stepping fluctuations, which would require a different analysis. If the primary configuration is that in Figure 1A, then the evidence of different excluded volume fractions between formins is rather weak, based on just the last 50 ns or less of the simulation (I may be missing something but there seem to be another 100 ns of these simulations in Figure 4. Shouldn't they be included in Figure 3?). The difference between formins is more clear in the configuration of Figure 1D, however this may not be primary configuration.

* A transient change of the system is to be expected each time a new formin FH2 is simulated. Given that the blocked volume fraction is relatively small for the all atom simulations in Figure 3, it appears to me that studies of the relative motion of just 2 formins with respect to Bni1 may not be sufficient to establish a completely convincing trend (to simplify the argument, it's 25% chance to get two heads, tossing a coin twice).

* Since the steric hindrance effect in the AA MD simulations is relatively small, one cannot be certain on its effect on actin polymerization kinetics. A steric hindrance blocking is a likely possibility but it's also conceivable that incoming actin monomers interact with the FH2 domain in a way that guides them to the barbed end. These aspects are not studied in this paper.

* It's not clear that the three models (all atom MD, metadynamics, coarse grained) provide a coherent story. The magnitude of the steric hindrance effect as well as the FH2 motions calculated by the CG simulations is much larger compared to the AA MD simulations. This seems to suggest that either the AA MD simulations need more time to explore a larger region of space or else that the CG simulations provide unphysical motions and thus cannot be used to calculate the steric hindrance effect. It's also not clear to me why the metadynamics studies were not used to calculate the effect of steric hindrance and actin helical twist.

* The timescale of 200 ns in Figure 1 appears to be too short to reliably predict secondary structure formation at the lasso, post and knob regions. For example, α helices typically take 50-100 ns to form in MD simulations and higher order structures may take even longer.

Reviewer #2:

This manuscript by Aydin and coworkers presents results from molecular dynamics simulations, addressing the conformations of formin FH2 dimers and actin subunits at/near the barbed ends, particularly focusing on barbed end "gating", i.e. the FH2 dimer's ability to allow or prevent the addition of a new actin subunit. The authors find that three factors contribute to gating, with different amplitudes for different formin isoforms: steric interference, flattening of the actin helix, and the strength of the interaction between FH2 and the barbed end.

While I disagree with the authors' argument that "In contrast to gating, much is already known about the transfer of profilin-actin from binding sites on FH1 domains to open barbed ends" (in their rebuttal of the "informal review") I do agree that gating is an important property that needs to be better understood. I also agree that MD simulations are a valuable method to do so, and I find their results interesting. However, I think the authors could in general better present their results in the context of existing models. As they are, their results are often difficult to connect to what we currently understand about formin activity.

I think this work should be of interest to readers beyond MD simulations specialists, if the authors improve their manuscript by addressing the following points.

1) Two main models are currently available (and often used to understand experimental data – see for example the recent Kubota et al., 2017) to describe FH2 gating and filament elongation: the so-called "stair-stepping" and "stepping second" models. They are extensively presented in a series of papers by Paul and Pollard from 2008-2009. It is frustrating that the current manuscript does not provide any additional insight on this question, which seems central here.

Can the present simulations shed light on these models? Do they favor one model over the other?

Hemidimer translocation is never explicitly mentioned. Is it nonetheless included in the present simulations, and if not, how would one integrate it?

2) I understand that, as written in the last sentence of the manuscript, the conformations fluctuate rapidly. But what time scales are we talking about? Are the fluctuations shown in this manuscript large enough to account for the equilibrium between open and closed states, or should we expect these transitions to take place over larger time scales?

3) Fluctuations and the FH2 dimer's ability to explore different conformations are addressed more explicitly in Figure 6 and in the subsection “Conformational mobility of FHT domains is consistent with the strength of intermolecular interactions”, where it is written that "Cdc12 FHT domain explores a smaller area than Bni1 and mDia1 FHT domains". However, these results seem in contradiction with those of Figure 7, where the FHT of Cdc12 has larger fluctuations and larger displacements than mDia1 and bni1. Please clarify.

4) In the Introduction, the gating factor is defined as the "fraction of the time that the FH2 domains are found in the open state". This is assumed to be the same as the gating factors determined as the ratio of the formin elongation rate to the free barbed end elongation rate (in the absence of profilin). However, equating these two definitions relies on one important hypothesis: that the on-rate constant for monomer addition is the same for a free barbed end and for an open-state formin barbed end. This should be specified. It should also be discussed in light of the present results: does this hypothesis appear valid, now that we know more about the conformations adopted by the filament in interaction with an FH2 dimer?

5) Gating is a schematic, all-or-nothing frame to work in. For instance, the open and closed states are generally defined by the 167° versus 180° twists of the filament. These extreme angles do not appear to be reached in the simulations, which thus seem to describe intermediate situations. Please comment. For example, should we rather consider a continuum of states, with different on-rate constants for the addition of actin monomers?

6) The simulations do not impose any constraint (boundary conditions) on the last subunits (A6 and A7 in the seven-mer) which thus correspond to the free pointed ends of very short filaments. The results (e.g. Figure 4 on twist angles) indicate that changes in conformation propagate over several subunits. One would then expect different results for longer filaments, which could perhaps be simulated by imposing the canonical filament conformation as a boundary condition. Please comment on this limitation of the model. How would the results extrapolate to longer filaments?

7) FH2 dimer detachment from barbed ends (Figure 8) is quite puzzling. What should one make of this? Do the authors expect this result to correspond to formin detachment from barbed ends (which appears to have a very low off-rate constant in experiments) or does it illustrate a limitation of the coarse grain method?

Reviewer #3:

Overall, the goal is of this paper, to use MD to test models of formin gating is an important one. However, the approach and presentation leave a lot to be desired. The topic is suited for a broader audience but the paper is not written with a broad audience in mind. Connecting the data to the model, simply in terminology, would have helped. Is the structure with a 5mer of actin expected to relax into a "closed" state? Is the structure with the 7mer of actin forced into an "open" state? This brings up questions about steric clashes observed when AA MD calculations were performed – Shouldn't the clashes be disallowed?

In general, the data are presented as lists, leaving it to the reader to interpret everything and/or guess how the authors are interpreting the data. My read doesn't agree with the final conclusions of the authors but I can't figure out why. For example, when looking at contacts, Bni1 was often more like Cdc12, which fits with the published gating data. However, when considering actin orientation, Bni1 was more like mDia1. Yet, the authors conclude that their data agree well with experimental gating data and that both steric clashes and actin twisting play a role in gating.

The paper was originally criticized for being entirely computational. The authors counter that the data correlate nicely with "wet" data in the literature but the correlations aren't as clean as the authors would have us believe. Further, they remain merely correlations until someone demonstrates that a manipulation to the proteins (in vitro and/or in silico) produces the predicted results. Along these lines, some of the work felt circular. It might have helped if the authors used the other co-crystal published (FMNL/actin) in addition to the Bni1/actin structure.

A second criticism was about focus on elongation/gating, which was not a concern for me. However, the authors state the FH1 domains can overcome the effect of gating but this study is done in the absence of FH1 domains, raising the question of how valuable it is. This is a point that needs to be addressed.
