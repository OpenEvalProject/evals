# Peer review - Round 1

Editors:
- Jennifer G DeLuca, Colorado State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48787.sa1](https://doi.org/10.7554/eLife.48787.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Edelmaier et al. describe a computational simulation of mitosis in the fission yeast Schizosaccharomyces pombe that includes bipolar spindle assembly, chromosome capture by spindle microtubules, chromosome bi-orientation, and kinetochore-microtubule attachment error correction. Their model provides a comprehensive view of mitotic cell division and proposes a set of rules that helps explain how mitosis is executed in fission yeast and possibly in metazoan cells, whose spindles are likely to be governed by similar fundamental principles.

Decision letter after peer review:

Thank you for submitting your article "Mechanisms of chromosome biorientation and bipolar spindle assembly analyzed by computational modeling" for consideration by eLife. Your article has been reviewed by Anna Akhmanova as the Senior Editor, a Reviewing Editor, and two reviewers. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Edelmaier et al. describes a computational simulation of spindle assembly, chromosome alignment, and chromosome segregation in S. pombe. The authors combine and extend their previous modeling efforts regarding fission yeast spindle assembly and chromosome bi-orientation to produce a new model that explains well: (1) the initial establishment of spindle bipolarity, (2) spindle stability and elongation during metaphase, and (3) kinetochore capture and attachment by MTs. The model, which encompasses all phases of mitosis in fission yeast, is currently state-of-the-art for the field and represents an important advance. However, several issues were raised by the reviewers which require attention. These are listed below.

Essential revisions:

1) The representation of error correction in the model should be re-examined. The destabilization of incorrect attachments is suggested to represent the activity of Aurora B kinase. However, this would require the enzyme to somehow respond to a highly complex property of the attachment – i.e., is it attached to a microtubule emanating from the correct pole? In comparison to all the other rules included in the simulations, which seem physically plausible, this particular rule seems rather ad hoc, unrealistic. How can an enzyme distinguish correct from incorrect? Simpler ideas have been suggested in the literature that might explain how Aurora B destabilizes incorrect attachments. For example, it might act selectively on kinetochore-microtubule attachments that lack force. The authors should consider this, or other, more mechanistic rules for error correction.

2) The simulated spindles fail to assemble and elongate in the absence of crosslinker Ase1 (Figure 2K). Because a force-balanced constant metaphase spindle length is evident in the cell, and because spindle assembly is achieved without the crosslinker Ase1, the impact as predictive power of the model/simulation is limited. The authors should explore additional simulation parameters that produce Ase1 spindle results in their model that are consistent with published experimental results.

3) The final metaphase spindle lengths observed in the simulations may not be a natural consequence of the force-balance inherent in the spindle, but instead due to the simplifying assumption that the nuclear envelope is defined as a rigid sphere. While the reviewers acknowledge that including flexibility of the nuclear membrane would likely increase the computational requirements of the model significantly, textual revisions acknowledging the limitations of the current model in regard to this point are needed.

4) The model used ~200 Kinesin-5 and Kinesin-14 motors, and ~600 Ase1 crosslinkers for the simulations. These numbers are 5x to 15x less than reported values existing in fission yeast (PomBase). The usage of simulation parameters different from experiment measurements undermines the impact of the model. The authors should either address this in their simulations or explicitly acknowledge the caveat of including lower levels of motors and crosslinking MAPs in the model compared to what has been measured experimentally.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Mechanisms of chromosome biorientation and bipolar spindle assembly analyzed by computational modeling" for further consideration by eLife. Your revised article has been evaluated by Anna Akhmanova (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance.

In subsection “Single model perturbations recapitulate the requirement for kinesin-5 motors and CLASP”, the authors added extensive revision on the role of Ase1 crosslinker (and pliable nuclear envelop). Specifically, they stated that in their model, the motor Klp9 can also act as a crosslinker in the absence of Ase1. Therefore, the removal of Ase1 would still produce a bipolar spindle, due to the action of Klp9. Reported data from several labs (McCollum, Millars, Toda, Tran) clearly showed that Klp9 does not function until anaphase. Thus, the authors cannot model the absence of Ase1 as still having crosslinking via Klp9.
