# Peer review - Round 1

Editors:
- Jonathan P Staley, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70534.sa0](https://doi.org/10.7554/eLife.70534.sa0)

This study extends previous work from the same group on the mechanism of 5' splice site recognition by the U1 snRNP using co-localization single-molecule spectroscopy. Compelling experimental and analytical approaches yielded three important conclusions: (1) the association of the U1 snRNP with the 5' splice site is largely determined by the snRNP itself and does not require other splicing factors; (2) sequence features of the 5' splice site determine whether a short-lived complex with U1 dissociates or transitions into a longer-lived, "productive" complex, potentially mediated by stabilized contacts with U1 associated proteins; and (3) the ability to form the longer-lived complex cannot be accurately predicted by base-pairing potential alone, as presumed by many predictive algorithms. This work will be of interest to colleagues in the splicing field as well as to others in fields where nucleic acid recognition by snRNPs plays a major role.


---

# Peer review - Round 1

Editors:
- Jonathan P Staley, https://ror.org/024mw5h28 University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70534.sa1](https://doi.org/10.7554/eLife.70534.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Multi-Factor Authentication of Potential 5' Splice Sites by the Saccharomyces cerevisiae U1 snRNP" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Jonathan P Staley as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Kevin Struhl as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Nils Walter (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The authors implicate protein in favoring the long-lived complex studied, imposing asymmetry of importance in base pairing, decreasing the stability of base pairing, and favoring base pairing length over thermodynamic stability. The authors further speculate a role for protein-RNA contacts involving Ych1 and Luc7, given informative, published structures. To corroborate the importance of protein in these features of 5' splice site recognition and to sharpen the mechanistic focus of the manuscript, the authors need to test the impact of Yhc1 and Luc7 mutants at the protein-RNA interface for roles in these features – especially Yhc1, given that the authors have already published on the impact of mutations in Yhc1. Otherwise, given the extensive work the authors have previously performed to already demonstrate that U1 snRNP binds to a 5'SS reversibly, with fast and slow dissociation events, one could argue that the current work falls somewhat short in providing new major biological insights.

2) On a related point, in the section describing U1/5'SS duplexes destabilization in U1 snRNP (line 281) an underlying assumption is that the binding of two RNAs (in the absence of the spliceosomal proteins) would share the same characteristics or trends as two identical RNAs incorporated into the U1 snRNP. While this may be a rhetorical device to increase the clarity/connection between the concepts of predicted binding free energies and the residence time of hybridized oligonucleotides, it does not address the possible reasons for the discrepancy observed in RNA oligonucleotide versus U1 snRNP binding. Further, in the Discussion (lines 395-398), the authors mention that while this study cannot identify a specific interaction or event that stabilizes the long-lived complex, structural studies implicate two U1 associated proteins: Yhc and Luc7. They further describe the interactions that could be implicated based on their findings. It is very difficult to follow this description of the contacts in the context of the larger snRNP structure without an illustrative figure. The authors should point to a reference and derive a physical model from the available cryo-EM structures to show that the U1 snRNA is, most likely, being constrained by its associated proteins in such a way that it increases the binding affinity to complementary RNA oligonucleotides. It would be helpful to add a figure based on the plethora of existing structural data to contextualize the findings of the current work (U1 SSRS/5'SS duplex), showing the protein contacts that the authors implicate in the conformational and thermodynamic modulation of the U1 SSRS/5'SS duplex.

3) Since splice sites are often "found" in the context of alternative or pseudo/near-cognate splice sites, it would be relevant to the biological significance of the study to ask whether the "rules" identified in the experiments presented in this study influence splice site competition and whether both the short- and long-lived states are subject to competition or, rather, only the short-lived complexes. If possible, it would be beneficial to repeat the CoSMoS experiment with two oligomer sequences of different colors or to assess the impact of adding an unlabeled competitor.

4) While the two-factor authentication metaphor of Figure 7 is charming, it seems off-topic. Instead, the authors should review the literature for examples of short, exploratory binding events involving an RNA:protein complex, followed by more stable, accommodated binding events, see e.g., the work by Sarah Woodson on 30S ribosomal subunit assemble and on Hfq function, work on kinetic proofreading of the ribosome, work on Cas9-based recognition of its target site, and many others. A potential descriptive framework to be used here is that of "conformational proofreading". Further, the use of "multi-factor authentication" seems inappropriate for a research article title.

5) The model described in the paragraphs starting with line 262 through 280 to interpret the observation of long and short complex lifetimes is not entirely clear. There are at least two potential models that can be considered to fit the observations: a linear and a circular model. A linear model would be one where U1 and substrate RNA are not associated (state 1), then they partially associate (state 2), and finally they isomerize to the completely associated/fully hybridized complex (state 3). The circular model is the same, except that it would additionally allow switching between states 1 and 3 directly (bypassing the partially associated state). To differentiate between these two scenarios, the authors would have to vary the concentration of the RNA probe and see if there is a uniform change in a single kon rate or if two kon rates start to appear. These rate subpopulations would be much easier to detect by fitting with hidden Markov models. It would seem unjustified to decide between these two models without obtaining such additional supporting data.

6) There is significant concern that the single molecule sampling rate used to acquire the CoSMoS data is too slow to accurately measure the shortest lifetimes observed, which are only ~10 seconds long. According to the Nyquist sampling criterion, the sampling rate needs to be (at least) twice the frequency of the event being measured, implying that the authors cannot meaningfully observe any lifetime shorter than ~10 seconds given their limited sampling rate. Further considering that at minimum two consecutive data points are needed for observing a 10 second lifetime, artifacts (e.g., camera noise) could make up a disproportionate amount of the signal observed in their data for these short lifetimes. For an accurate measurement, the authors need to repeat the experiments at a higher sampling rate to make sure that there are no faster, transient interactions than those currently reported, and that the values reported are accurate.

7) The authors have chosen to extrapolate rates via exponential fitting to dwell time distributions. This is a reductive approach that ignores the relationship between consecutive events. It is strongly recommended that the authors consider using a hidden Markov modeling (HMM) approach instead. HMMs have long become the gold standard in single molecule biophysics. Even better, a Bayesian approach could help analyze entire datasets at the same time. In this reviewer's opinion, the ebFRET software package from the Gonzalez lab at Columbia University could, for example, work well here.

8) The authors should say more about the particular requirement for basepairing at position 6, especially in the context of the experiments in Figure 5. This is particularly striking as this position is not well conserved in natural 5'ss, at least compared to position 5.
