# Peer review - Round 1

Editors:
- Christopher P Hill, University of Utah School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62021.sa1](https://doi.org/10.7554/eLife.62021.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript reports the unexpected finding that the NADase SARM1, a mediator of axon loss in response to injury, is inhibited by binding of NAD+ substrate to an allosteric site. NAD+ is seen to stabilize an ordered conformation of catalytic domains at the periphery of the octameric assembly. This arrangement prevents formation of active catalytic domain dimers, thereby providing an explanation for regulation of the energetic collapse caused by SARM1 activation.

Decision letter after peer review:

Thank you for submitting your article "The Structural Basis for SARM1 Inhibition, and Activation Under Energetic Stress" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Christopher P Hill as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by John Kuriyan as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jonathan Elegheert (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

SARM1 is an enzyme that depletes NAD+ to trigger axon loss in response to injury. A recent publication reported the structure of full-length SARM1 to reveal an octameric ring assembly. The current study also reports structures of full-length SARM1 (inactive mutant) by cryo-EM, and makes the additional finding that SARM1 is substrate-inhibited. Structures determined after crosslinking in the presence of glycerol or the presence of NAD+ appear to be an inhibited conformation. Biochemical studies show that glycerol and NAD+ (and ATP) are inhibitors, and NAD+ binds an allosteric site to prevent the catalytic domains adopting their active dimeric association. In contrast, a structure determined in the absence of NAD+ or crosslinking allows enough conformational freedom for catalytic domains to dimerize. Overall, this is an important advance in structural-mechanistic understanding.

Essential revisions:

1) Please discuss the recent Bratkowski et al. publication in Cell Reports from 2020 explicitly, which reports similar structure determination but arrives at a very different mechanistic conclusion.

2) A major point of the paper is on the NAD-mediated allosteric inhibition of SARM1. To strengthen this point, it may be helpful to expand the discussion and include more figure panels that illustrate how NAD binds SARM1, and how this binding stabilizes the autoinhibited conformation. Given the limitations of data, the best way to illustrate and discuss will be a judgement call for the authors. We note that the density for NAD as shown in Figure 5 is a bit weak, with a part of the NAD molecule sticking outside of the density. Is it possible to fit NAD in the opposite orientation? In addition, would it be helpful to show comparison the ARM/TIR interface with or without NAD in more detail, which may shed more light on how the NAD-induced conformation of ARM holds tighter to TIR.

3) As pointed out the manuscript, the results from mutations at the NAD binding site are somewhat unexpected. L152A, which has a strong effect, appears not directly contacting NAD. R322 and R157 also seem a little far from NAD. Plus, these residues are not conserved in C. elegans SARM1. In contrast, W103 is conserved and appears to be making a key interaction with NAD, but its mutation has no effect. Related to this point, the recent Cell Reports manuscript shows essentially the same autoinhibited assembly of SARM1, in the absence of Grafix crosslinking or NAD, which seems to argue that the SARM1 is able to adopt the autoinhibited conformation on its own. These discrepancies raise the possibility that in cells a different metabolite binds to this site in SARM1, with similar but distinct atomic interactions. Or is it possible that the NAD-mediate regulation is species specific?

4) The secondary TIR docking site is disengaged in the NAD-bound structure. Can the authors discuss whether this reflects the actual difference between the two states of the protein, or is it possible that the secondary docking site is imposed by the crosslinking reagent?

5) The resolution based on the FSC between the density map and model for the NAD-bound structure is 5.6 Å, much worse than the resolution of the map based on the gold-standard FSC (2.7). This large difference between the two FSC curves is concerning, suggesting that there are some issues in the model that cause it to not fit the density well. This issue needs to be addressed, and the PDB-vs-map FSC curves should be shown as supplemental figures. The manuscript does touch on this point, mentioning "domain-based heterogeneity", but fell short of providing a clear explanation. One possibility might be that NAD only occupied some, but not all, of the subunits in the octamer, which resulted in different conformations of the peripheral TIR and ARM domains within the same octamer. Imposing C8 symmetry under this situation would deteriorate the density for all the subunits. Have the authors tried the symmetry expansion and then focused refinement approach as implemented in Relion (http://dx.doi.org/10.1016/bs.mie.2016.04.012)? One might then perform classification of the subunit, which may allow subunits with different conformations to be separated.

6) The HEK-based viability assay has been used in previous studies to assess SARM1 activity and the effect of various mutations and domain deletions. Hence, the authors adopted it for this work. Although the experimental setup is internally controlled (accounting for fluorescent background signals and emission from mock-transfected cells), there is no control over or validation of mutant protein expression levels (assessed using e.g. blot densitometry), which may skew the cell viability data if expression levels would diverge from wild-type levels, by impacting on NAD depletion rates. Overall, the effects of various SARM1 mutants would be more elegantly assessed using a robust neuronal assay, where SARM1 variants would be expressed in a more native-like environment and axonal death would be monitored. Although desirable, this is not necessary for the revised manuscript.
