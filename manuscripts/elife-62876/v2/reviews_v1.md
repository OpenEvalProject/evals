# Peer review - Round 1

Editors:
- Thomas Surrey, Centre for Genomic Regulation (CRG) Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62876.sa1](https://doi.org/10.7554/eLife.62876.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This interesting study addresses the question of how the microtubule cytoskeleton reorganizes in the immunological synapse. Using a variety of experimental techniques, including expansion microscopy, and computer simulations, the work demonstrates an important role of microtubule length control by the kinesin-4 KIF21B for correct T cell polarization during immunological synapse formation, providing new insight into the molecular mechanism of this important process.

Decision letter after peer review:

Thank you for submitting your article "Kinesin-4 KIF21B limits microtubule growth to allow rapid centrosome polarization in T cells" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Vivek Malhotra as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Alex Mogilner (Reviewer #1); Michael L Dustin (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments and modeling may be required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

This is a very interesting study addressing the question of microtubule cytoskeleton reorganization in the immunological synapse. Specifically, the work demonstrates the contribution of KIF21B for the control of the T cell microtubule (MT) network required for T cell polarization during immunological synapse formation. The authors use a variety of microscopy techniques, including expansion microscopy, controlled perturbations of the cell, and computer simulations to generate their results. The authors show that knockout of KIF21B results in longer MTs that result in an inability to polarise the MT network by a mechanism consistent with dynein motor function at the immunological synapse to capture long MTs and center the MT aster at the synapse. They use the Jurkat cell line, which is a classical model for this step in immune synapse function and fully appropriate. They show that KIF21B-GFP can rescue the knockout phenotype and then use this as a way to follow KIF12B dynamics in the Jurkat cells. KIF21B works by inducing pausing and catastrophe, thus, more MTs are shorter when present. They also rescue the defect in the KIF21B KOs with 0.5 nM vinblastine, that directly increases catastrophes, shortens the MTs and restores MT network polarization to the synapse. As a functional surrogate they investigate lysosome positioning at the synapse, which is one of the proposed functions of this cytoskeletal polarization. The use of expansion microscopy in this system is relatively new and clearly very powerful. The modelling component adds to the story and supports the sliding model proposed by Poenie and colleagues in 2006, but cannot say that there is no component of end capture and shrinkage as proposed by Hammer and colleagues more recently. Experiments and modelling are performed to a high standard and the results advance the field.

Essential revisions:

1) The author use poly-D-lysine (PDL) to attach the Jurkat cells to the coverslip as a "control" condition. Do the authors also observe polarization of the MT cytoskeleton in these experiments? The intention is probably to have a random orientation, but it has been found that charge-based adhesion zones can activate T cells due to differential exclusion of CD45 and TCR or other effects (see PMID: 29476188). Please always state when PDL + anti-CD3 is used PDL or was a control antibody used? This should be stated in each case as its not necessarily neutral for these sensitive cells. If the authors have data on polarization on PDL they should report this in supplementary figures. If there is potential activation in this condition based on some non-random polarization then it would be useful to briefly discuss this as the questions being asked don't really rely on the cells being "resting" or "activated", although things like Ca2+ flux might affect the function of KIF21B.

2) The authors use a mathematical model and this theoretical part was well performed. The authors have done a good job of discussing the earlier work from Poenie with polarization microscopy that favoured the sliding model and the recent work from Hammer that suggested the end capture/shrinkage model might better fit direct observations, but neither study provided relevant perturbations to test the models. Another recent modelling study in Biophys J seems to support a mix of the two mechanisms being relevant – PMID: 31084903. It seems intuitive that the sliding model works if all the circumferential MTs are <πr in length but becomes problematic when MTs are in the πr->2πr length range, where a "tug of war" can happen. It seems like there are lots of MTs >πr length in the KIF21B KO based on data in Figure 2G. Probably this has been corrected for the expansion and relates to lengths in the native cells. The model doesn't seem to fully capture this as even without any KIF21B the length is 12 µm- which is similar to wildtype/no perturbation rather than the estimated values for the KIR21B KO of ~ 30 µm. What happens if parameters are adjusted to allow longer MTs to form in the model in both WT and KIF21K KO setting? This could be explored by additional simulations or by a discussion if deemed beyond scope.

3) The model nicely integrates and explains the data, but is it predictive? A detailed model like the one here clearly can generate some nontrivial prediction that could either be experimentally tested here or proposed to be tested in the future.
