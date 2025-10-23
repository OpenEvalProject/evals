# Peer review - Round 1

Editors:
- Ronald L Calabrese, Emory University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.12741.031](https://doi.org/10.7554/eLife.12741.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "A hindbrain control system for exploratory locomotion" for consideration by eLife. Your article has been favorably evaluated by three reviewers, including Mark Masino and Ronald Calabrese, who is a member of our Board of Reviewing Editors. The evaluation was overseen by Eve Marder as Senior editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This research report presents a technological tour de force, in which the authors use light-sheet laser imaging techniques to identify neurons in the larval zebra fish brain that bias turning direction. The authors present convincing evidence that two bilateral clusters of neurons in the anterior rhombencephalon (ARTR) are asymmetrically active during runs of same direction turns. In a uniformly lit clueless arena, free-swimming larvae tend to make runs of turns in the same direction and switch stochastically to runs of turns in the opposite direction. Such turning bias can be observed in fictive swim preparations. Ipsilateral neuron clusters in the ARTR are coactive with runs of turns to the same side. One of the clusters is shown to be GABAergic and the other glutamatergic. The GABAergic cluster projects contralaterally and is hypothesized to set up mutual inhibition between bilateral clusters. A minimal network model based on positive feedback to the ipsilateral cluster when a turn is made that decays slowly and mutual inhibition across the midline can reproduce the observed switching turn bias. A two state Markov model based on this minimal model can reproduce behavioral tracks.

The data are extensive and appropriately analyzed with relevant statistics. The Figures are easy to assimilate and the legends clear. Supplementary data answers for almost all controls. Materials and methods is extensive and complete.

Despite the demonstrable strengths of the manuscript, at present it claims to do much more than it actually achieves. Therefore, we feel that the present manuscript should be revised to describe clearly what it has accomplished, and that the authors should consider doing the considerable follow-up experiments and submitting them either as a Research Advance to this paper, assuming this one is successfully revised, or as an additional stand-alone paper, as described below.

Essential revisions:

There are two classes of concerns that make this paper more suitable as a proof of principle that the methods can reveal putative behaviorally relevant neurons in free moving fish and behaviorally relevant preparations.

1) How the behavior studied is controlled is not well discussed despite the modeling.

A) It remains unclear how the activity of the ARTR is initiated and terminated and how the switch of the activity between the left and right sides is mediated.

B) The authors show that ARTRs project to some reticulospinal neurons, however it is still unclear if these neurons are the ones relaying the turning commands to the spinal cord. Ablation or optogenetic activation of these neurons should be used to test this.

2) The claim that the ARTR neuron clusters direct biased turning is based on correlation; neither necessity nor sufficiency of the ARTR neurons is shown for directing turning bias.

A) We are not given an estimate of the number of neurons in the ARTR clusters so the results of ablations/activations are hard to evaluate critically. The effect of ablations on turning bias are small; this concern pertains both to the turn bias (Figure 4B) and randomization of turn sequences (Figure 4E, F, G). It is hard to see the ARTR cells as necessary for turn bias with such small effects.

Inexplicably, only the medial cluster was ablated (why?) when the inhibitory neurons of the lateral cluster should have the bigger effect. There should also be a bigger effect for more cells ablated and the effect of number of cells ablated on outcome was not evaluated.

B) The optogenetic stimulation experiments are not totally convincing. 15-20 cells in a cluster are stimulated but we are not told what portion of the cluster population this represents. Moreover, the effects are not inconsistent with simple motor commands. Only Figure 5—figure supplement 2 differentiates these cells (both medial and lateral clusters presumably?) from more 'downstream' motor commands (vSPN cells) and the time course effect is not large. The Ca responses in the ARTR cells are slower, but is this truly indicative of activity or Ca dynamics, and is it large enough to differentiate these cell types functionally? (We are not even told if the ARTR cells imaged are medial or lateral cluster cells.). The explanation in Discussion for why the stimulation experiments affect turn amplitude is not convincing.

C) A more complete set of ablation and activation experiments is needed to convincingly indicate necessity and sufficiency of the ARTR cells for directing biased turning. While these are beyond the scope of this submission, these experiments could constitute a nice Research Advance paper in eLife in 6 months or a year's time.

i) Specific ablations of medial and lateral ARTR cells (glutamatergic vs. GABAergic neurons) with assessment of the% of the population deleted, both unilaterally and bilaterally. How do bilateral lesions affect free swimming behavior?

ii) The authors show that ARTR project to some reticulospinal neurons, however it is still unclear if these neurons are the ones relaying the turning commands to the spinal cord. Ablation or optogenetic activation of these neurons should be used to test this.

iii) There are other regions that are equally active during the swimming activity such as Rh4-6 of a region in the caudal brainstem (caudal to IO, Figure 3A). The authors do not consider that these regions contribute as much as ARTR to the behavioral pattern. However, there is no experimental support of this assumption. Ablation and stimulation of these regions should be tested to exclude they potential contribution to determining the swimming direction.

There is a more minor technical concern in addition. We are not convinced that the difference in the amplitude of the fictive activity (Figure 1G) can be used as a proxy for turns. The first burst on the side of the turn is always larger and this will affect the fit and the power of the activity. The authors should analyze the duration of each burst that should be larger on the side of turn compared to the contralateral side.

Recommendation:

The authors should refocus the paper in light of the concerns above. Present the work as a major step forward in the identification of neurons involved in a complex behavior without declaring that the ARTR neurons are the main players in the control of swim turn bias. Rather the experiments to date (Ablation and stimulation) point to these neurons as important candidates that at least contribute control. In this regard the authors may want to eliminate the modeling, holding it back for a future Research Advance paper. We are taking this position because of eLife's general philosophy to not require many months or extensive new experiments for a paper. The reviewers felt that this paper, in principle, deserves publication, but only if it is revised to more correctly represent what it has actually demonstrated, which is considerably less than claimed.
