# Author response - Round 1

Authors:
- Qin Wang
- Huaxun Fan
- Feng Li
- Savanna S Skeeters
- Vishnu V Krishnamurthy ([ORCID: 0000-0001-9905-5965](https://orcid.org/0000-0001-9905-5965))
- Yuanquan Song ([ORCID: 0000-0001-7699-2059](https://orcid.org/0000-0001-7699-2059))
- Kai Zhang ([ORCID: 0000-0002-6687-4558](https://orcid.org/0000-0002-6687-4558))

## Response text

DOI: [10.7554/eLife.57395.sa2](https://doi.org/10.7554/eLife.57395.sa2)

Essential revisions:

1) This study assumes that the tools trigger signaling pathways independently of upstream (neurotropic) signaling. However, whether these tools require some upstream signaling remain incompletely addressed. For example, activation of Raf1 requires upstream activation by kinases phosphorylating the N-terminal region (Y341 and S338). The phosphorylation of S338 is a commonly used read-out for Raf-1 activation (and mutants at this position show no activation). It would be very informative to examine the status of pS338 in optoRaf and to compare the optoRaf to a mutant S338A version, at least in Hek293 cells. Because these phosphorylations are linked to Raf dimerization, these studies would provide insight into whether Raf dimerization is required or possible in this context.

This is an excellent point. As suggested, we have performed Western blot in HEK293T cells using an antibody against phosphor-S338 of Raf1 under the optogenetic stimulation conditions. As a positive control, we used serum stimulation. As expected, in cells transfected with the optoRaf S338A mutant, optoRaf S338A cannot be phosphorylated at this site regardless of serum and light stimulation (Figure 1—figure supplement 1E, top panel). Importantly, unlike wild-type optoRaf, optoRaf S338A significantly abolished the light-dependent activation of ERK (Figure 1—figure supplement 1E, third panel). This result indicates that activation of optoRaf should require the upstream activation machinery. Furthermore, as suggested by the reviewer, it is very likely that Raf dimerization is involved in the activation of optoRaf.

2) It would be also helpful to include more specificity controls for Raf vs. Akt signaling in Drosophila neurons to ensure the signals directly go to cells where the functional assessments are being conducted.

Thanks for the suggestion. To make sure that light-mediated enhancement of Raf and AKT signaling occurs specifically in the target cell, we used DAPI staining to identify da neurons with or without the corresponding optogenetic systems. As shown in Figure 2—figure supplement 2, within the field of view, only C4da neurons marked by ppk-CD4tdGFP express optoRaf or optoAKT, which is under the control of ppk-Gal4, an enhancer driver for C4da neurons. In these cells, blue light-stimulation significantly enhances the level of phospho-ERK or phospho-p70 ribosomal S6 kinase (phospho-p70S6K) compared with the neighboring cells, which do not express optoRaf or optoAKT (DAPI only, no GFP). This result confirms that blue light specifically triggers Raf/MEK/ERK or AKT signaling in optoRaf/AKT expressing C4da neurons.

3) The kinetic experiments are interesting but somewhat incomplete, and it is unclear what the takeaway from these experiments should be. Importantly, it is not known how different pulsed light patterns translate temporally to signaling. It seems that from the data in Figure 1, it is possible that in neurons patterns may maintain a constant activation of the pathway. Additional controls looking at the extent of signaling in neurons with these paradigms would be really helpful.

We really appreciate the insightful comments. As suggested, we carried out a kinetic study in C4da neurons to determine if intermittent light pattern leads to intermittent signaling activity. The level of ERK and AKT signaling activities was probed by immunostaining of phospho-ERK and phospho-p70S6K, respectively. Consistent with the results from mammalian cell culture, 5-10 min of light stimulation was sufficient to activate optoRaf and optoAKT (Figure 2—figure supplement 1). After the light was off, the level of phospho-ERK and phospho-p70S6K decreases monotonically. We observed that optoAKT inactivates faster than optoRaf, i.e., level of phospho-p70S6K decreases to the basal level within 15 min, whereas phospho-ERK decreases slower (Figure 2). This difference in decay kinetics may arise from distinct signaling threshold, signaling capacity of Raf and AKT, or both.
