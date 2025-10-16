# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39694.046](https://doi.org/10.7554/eLife.39694.046)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for sending your article entitled "Chronology of motor-mediated microtubule streaming" for peer review at eLife. Your article is being evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by Anna Akhmanova as the Senior Editor.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond within the next two weeks with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

Summary:

This article describes a computational study of a model for cytoplasmic streaming, motivated by the phenomenology found in Drosophila oocytes. The authors introduce a coarse-grained model in which details of the molecular motors' activity that can lead to sliding between adjacent microtubules are subsumed into an effective orientation-dependent potential. The microtubules are modelled as linked spheres, and the whole setup is described by a Langevin equation. The results include many aspects of the correlation functions between the microtubules, with different regimes characterized by different types of alignments. Probability distribution functions of speeds are computed, of the kind that can be measured experimentally. The authors make some contact with experimental studies of streaming using PIV and advance the hypothesis that heavy-tailed velocity distributions arise without the previously conjectured need for varying motor speeds or complex cytoskeletal geometry.

Essential revisions:

1) Whereas the mechanism postulated by authors does produces streaming in the in silico system studied here, it is not guaranteed that the same mechanism occurs inside the cell or in vitro. Streaming occurs in a vast range of systems, from plants upwards, and in many of these systems the filaments are both organized and unchanging in their conformations. For sure in others the situation is different, but the present manuscript appears to suggest that cytoplasmic streaming is always associated with interfilament sliding, whereas that is not the case. This needs to be clarified.

The manuscript contains various measurements and predictions, but it is rather unclear which of them would unambiguously demonstrate the postulated mechanism if recovered in experiments. This point is crucial and should come across the manuscript with no ambiguity. In other words, the authors should clearly explain which one of their predictions an experimentalist should recover in order to verify that the mechanism behind MTs streaming is indeed that proposed in this paper.

There is a significant literature on the streaming problem in Drosophila that has not been cited. Examples include Woodhouse, et al., 2013 and Khuc Trong, et al. 2015, which discuss in detail self-organization processes and the role of cytoskeletal architecture on streaming patterns. Of particular interest in the case of Drosophila is the nucleation of microtubules from the periphery of the oocyte, leading to anchoring there. This is not accounted for in the present paper.

2) The authors do not explain what promotes short-ranged polar alignment in the absence of directed motion and cross-linking. In other words, why the polar bundles form in the first place? Can the authors exclude that the interlocking of the beads forming an individual MT has nothing to do with it?

3) While reading the manuscript, it is very tempting to think about the active suspensions of MT bundles and kinesin pioneered in the Dogic Lab. The authors do refer to some of this work and, toward the end of the manuscript, explicitly say that the collective motion found here resembles that observed in those experiments. Yet, it is rather puzzling that they avoid making a direct comparison. If the present numerical approach could serve as a particle model of these active suspensions, this should be clearly said and motivated (with an eye to the rich theoretical literature around the topic). If not, it would be useful to know where are the fundamental differences and how both these model systems compare to cytoplasmatic streaming in vivo.

4) It is somewhat unclear how the model outlined in Sec. II. reconciles with the non-equilibrium nature of kinesin-based propulsion. MT-kinesin interactions are modeled through conservative forces, that can be expressed as derivatives of of potential energy U_mot. Furthermore, the motor binding rate follows the Boltzmann distribution. This raises the question of whether the authors are attempting to describe cytoskeletal activity as an equilibrium process. Most models of cytoskeletal fluids (both discrete and continuous) are based on the assumption that kinesin moves at constant speed from the minus to the plus end (or vice versa for specific types of kinesin). This manifestly violates detailed balance and is consistent with experimental observations (see e.g. Schnitzer and Block, Nature 1997). One can debate on whether kinesin is in fact delivering a constant power, as opposed to move at constant speed, but both scenarios appear to lie outside of the scope of the present model.

5) The reviewers raised questions about the degree of novelty of your methodology. While recognizing that the specific results in the paper concerning sliding motility are new, they pointed to recent work published by the Shelley group (Nazockdast et al., 2017) which has introduced a 3D computational framework that accounts for polymerization and depolymerization kinetics of fibers, their interactions with molecular motors and other objects, their flexibility, and hydrodynamic coupling. Their model has been applied in (Nazockdast et al., 2017).

The present authors should clearly compare and contrast their work with these recent papers.

6) Regarding the simulations, the reviewers are unclear why a Langevin equation with a mass term was used in what is clearly an overdamped problem. It is also unclear why it is possible a priori to neglect hydrodynamic interactions between filaments, and the significance of working in only two dimensions. All of

these issues need clarification.

Reviewer #1:

This article describes a computational study of a model for cytoplasmic streaming, motivated by the phenomenology found in Drosophila oocytes. The authors introduce a coarse-grained model in which details of the molecular motors' activity that can lead to sliding between adjacent MTs are subsumed into an effective orientation-dependent potential. The MTs are modelled as linked spheres, and the whole setup is described by a Langevin equation. The results include many aspects of the correlation functions between the microtubules, with different regimes characterized by different types of alignments. Probability distribution functions of speeds are computed, of the kind that can be measured experimentally. The authors make some contact with experimental studies of streaming using PIV and advance the hypothesis that heavy-tailed velocity distributions arise without the previously conjectured need for varying motor speeds or complex cytoskeletal geometry.

The subject matter of this paper is certainly appropriate for eLife, and as a computational study it is reasonably well done. Less clear to me is the significance of the results. In part this is due to what appears to be a superficial understanding of the literature on streaming. Streaming occurs in a vast range of systems, from plants upwards, and in many of these systems the filaments are both organized and unchanging in their conformations. For sure in others the situation is different, but the present manuscript appears to suggest that cytoplasmic streaming is always associated with interfilament sliding.

Second, there is a significant literature on the streaming problem in Drosophila that has not been cited. Examples include Woodhouse et al., 2013 and Khuc Trong, et al. 2015, which discuss in detail self-organization processes and the role of cytoskeletal architecture on streaming patterns. Of particular interest in the case of Drosophila is the nucleation of microtubules from the periphery of the oocyte, leading to anchoring there. This is not accounted for in the present paper.

Regarding the simulations, I am unclear why the authors would solve a Langevin equation with a mass term in what is clearly an overdamped problem. It is also unclear to me why it is possible a priori to neglect hydrodynamic interactions between filaments, and the significance of working in two dimensions.

Overall, I think the contributions of this paper are interesting, but the lack of proper biological context is a significant weakness.

Reviewer #2:

The manuscript by Ravichandran et al. introduces a computational framework for studying microtubule (MT) dynamics with focus on motor-driven sliding motility. MTs are modeled as spring chains with standard stretching and bending energy contributions, and steric MT-MT interactions are described by WCA repulsion. Motor activity is modeled by cross-linker springs between MTs that bind with exponential rates depending on relative orientation between motors and MT pairs. The model neglects hydrodynamics and does not account for MT nucleation and de/polymerization, although both effects could likely be added in future extensions of this framework. Simulations are restricted to 2D systems. Simulated MT numbers are O(1000) and the authors make a commendable effort to provide biologically relevant values for all model parameters.

The paper is clearly written and the numerical study has been performed carefully.

My main concern regarding suitability for publication in eLife is novelty.

Recent work published by the Shelley group, see Nazockdast et al., 2017, has introduced a 3D computational framework that accounts for polymerization and depolymerization kinetics of fibers, their interactions with molecular motors and other objects, their flexibility, and hydrodynamic coupling. Their model has been applied in Nazockdast et al., 2017.

In view of this previously published work, I believe that the present manuscript does not constitute the type of major conceptual or computational advance typically expected for publication in eLife. That said, it seems to me that the specific results in the paper concerning sliding motility are new and certainly deserve publication in some other form.

Reviewer #3:

Ravichandran and coworkers report a comprehensive computational study of microtubules (MT) streaming. This process, observed both in vivo and in vitro, is generally ascribed to the sliding motion promoted by kinesin molecules, but the microscopic mechanism behind the kinesin-mediated MT-MT interactions is still debated. Numerical simulations suggest that streaming results from the interaction between bundles of polar-aligned MTs and is particularly sensitive to the time scale associated with the reorientation of individual MTs. The paper appears technically sound, clearly written and nicely illustrated. Unfortunately, there are various points where the authors have been too vague.

1) Whereas the mechanism postulated by authors does produces streaming in the in silico system studied here, it is not guaranteed that the same mechanism occurs inside the cell or in vitro. The manuscript contains various measurements and predictions, but it is rather unclear which of them would unambiguously demonstrate the postulated mechanism if recovered in experiments. This point is crucial in my opinion and should come across the manuscript with no ambiguity. In other words, the authors should clearly explain which one of their predictions should an experimentalist recover in order to verify that the mechanism behind MTs streaming is indeed that proposed in this paper.

2) The authors do not explain what promotes short-ranged polar alignment in the absence of directed motion and cross-linking. In other words, why the polar bundles form in the first place? Can the authors exclude that the interlocking of the beads forming an individual MT has nothing to do with it?

3) While reading the manuscript, it is very tempting to think about the active suspensions of MT bundles and kinesin pioneered in the Lab of Zvonimir Dogic and now investigated by various other groups around the world. The authors do refer to some paper by the Dogic Lab and, toward the end of the manuscript, explicitly say that the collective motion found here resembles that observed in those experiments. Yet, they avoid making a direct comparison. I find this puzzling. If the present numerical approach could serve as a particle model of Dogic's active suspensions, this should be clearly said and motivated (with an eye to the rich theoretical literature around the topic). If not, it would be useful to know where are the fundamental differences and how both these model systems compare to cytoplasmatic streaming in vivo.

4) It is somewhat unclear how the model outlined in Sec. II. reconciles with the non-equilibrium nature of kinesin-based propulsion. MT-kinesin interactions are modeled through conservative forces, that can be expressed as derivatives of of potential energy U_mot. Furthermore, the motor binding rate follows the Boltzmann distribution. This raises question on whether the authors are attempting to describe cytoskeletal activity as an equilibrium process. Most of models of cytoskeletal fluids (both discrete and continuous) are based on the assumption that kinesin moves at constant speed from the minus to the plus end (or vice versa for specific types of kinesin). This manifestly violates detailed balance and is consistent with experimental observations (see e.g. Schnitzer and Block, Nature 1997). One can debate on whether kinesin is in fact delivering a constant power, as opposed to move at constant speed, but both scenarios appear to lie outside of the scope of the present model.

In summary, whereas the authors have been quite meticulous in calibrating the parameters to experimental values, it is unclear to me whether what they present are indeed properties of MTs and kinesin or simply properties of their model. Therefore, I am unable to recommend this paper for publication in eLife in the present form.
