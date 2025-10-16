# Peer review - Round 1

Editors:
- Yukiko Goda, https://ror.org/02qg15b79 Okinawa Institute of Science and Technology Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80168.sa0](https://doi.org/10.7554/eLife.80168.sa0)

Berryer et al. report on an automated and quantitative platform to study the number of synaptic inputs formed in networks of human excitatory neurons and astrocytes in vitro. The utility of the platform was tested by screening a large collection of small molecules; several modulators of synapse density were identified and validated in follow-up experiments. The automated platform substantially extends what is currently available, particularly with respect to the automation of the initial analysis steps. The positive hits identified here, the inhibitors of bromodomain and extraterminal (BET) family of gene expression regulators, are important, and will likely contribute to the understanding of the mechanisms of human synapse assembly.


---

# Peer review - Round 1

Editors:
- Yukiko Goda, https://ror.org/02qg15b79 Okinawa Institute of Science and Technology Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80168.sa1](https://doi.org/10.7554/eLife.80168.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "An automated high-content synaptic phenotyping platform in human neurons and astrocytes reveals a role for BET proteins in synapse assembly" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Lu Chen as the Senior Editor. The following individuals involved in the review of your submission have agreed to reveal their identity: Matthijs Verhage (Reviewer #2); Carlo Sala (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All three reviewers have acknowledged the high potential of the automated platform in drug screening and related studies that target human synapses and the novelty of identifying BET inhibitors in affecting synapse density. Some shortcomings of the study have been raised, however. These relate to the limitations of using synapsin I as the sole synaptic marker and the fact that the manuscript could be considerably strengthened by providing further evidence in support of the synaptic actions of BET inhibitors and including statistical analysis to clarify and place limits on the power of the phenotyping platform in detecting small effects. To this end, the following essential revisions are requested, the first two of which require additional experiments. Furthermore, the authors are also requested to address all the points raised by each reviewer.

1) The use of synapsin1 as a sole synapse marker should be experimentally validated in two ways:

(a) In a sample set of experiments, demonstrate the extent to which postsynaptic markers are found apposed to synapsin I and that the distribution of postsynaptic markers match that of synapsin I.

(b) In a sample set of experiments, demonstrate the extent to which other presynaptic vesicle marker and/or active zone markers colocalize with synapsin I and that the distribution of other presynaptic markers match that of synapsin I.

2) The effects of BET inhibitor treatment on the expression of synaptic proteins should be confirmed by Western blots.

3) The synaptic gene expression programs boosted by BET inhibitors should be further characterized with respect to their pre/post expression loci or function (cf. Reviewer 2, major point 3).

4) Further statistical analysis should be performed to clarify the power of the platform in detecting the effects of a certain size (cf. Reviewer 2, major point 1).

Reviewer #1 (Recommendations for the authors):

Here the synaptic phenotyping involves three parameters: (i) density of a synapse marker protein, (ii) dendrite area, and (iii) number of viable cells. In particular, the key parameter, synapse density, is reliant on the density of a presynaptic phosphoprotein, synapsin I, whose synaptic function, at least in rodents, might be limited and whose confinement at presynaptic boutons is activity-dependent. Therefore, it is possible that the use of another synaptic marker (presynaptic or postsynaptic) may give different outcomes. In other words, the robustness of a platform based on synapsin 1 as the only synaptic marker is not entirely clear. Providing some experimental support to this end would make the manuscript more convincing (cf. specific points 1, 5).

1) What percentage of Synapsin puncta present on MAP2 are bona fide synapses in that they contain postsynaptic markers? While it may not be necessary to perform the double labelling each time, it would be helpful to know how accurately the readout of presynaptic maker density corresponds to the actual synapse density.

2) Figure 1e, f, and Lines 196-197: The claimed consistency of plating across batches of differentiation needs to be better substantiated. For instance, in panel e, there is a big difference between batches 3 and 4. What is the permissible range for the said consistency and the basis for choosing such criteria warrants an explanation?

3) Figure 3. In order to facilitate a direct comparison of the dosage effects of the drugs on synapsin I density, MAP2 neurite area, and cell survival, the x-axis should be the same across the three parameters.

4) Figures4, 5. The presence of astrocytes in promoting synapsin 1 density on MAP2 neurites is far more potent than the effects of small molecule inhibitors in facilitating synapsin 1 density. Moreover, the presence of astrocytes actually seems to reduce the MAP2 positive neurite area, which will further boost the synapsin 1 density measurement that is made relative to MAP2 neurite area. Could one exclude the possibility that an apparent lack of an increase by the small molecule inhibitors in the absence of astrocytes was because of sensitivity issue?

5) Figure 6. A direct demonstration of an increase in neurexin 3 and/or homer 1 protein levels by immunofluorescence labelling and western blots in the co-culture system used here following BET inhibitor incubation would further strengthen the conclusion of a role played by BET proteins in attenuating synapse formation.

Reviewer #2 (Recommendations for the authors):

1. The authors claim they "established a novel, automated, high-content synaptic platform" (line 402). While the extent of automation certainly reaches beyond what has been published, other aspects are not 'novel', especially the central concept of evaluating the density of synapsin1 puncta over MAP2 positive dendrites. It would be good to define a bit more precise the exact step beyond the state of the art, which lies mostly in the automation of plating etc, and to give credit to previous studies that have delivered open-source methods for automated synapse quantifications:

SynQuant https://doi.org/10.1093/bioinformatics/btz760,

SynapseJ https://doi.org/10.3389/fncir.2021.731333,

SynPAnal https://doi.org/10.1371/journal.pone.0115298,

SynD https://doi.org/10.1016/j.jneumeth.2010.12.011

2. For Figures2 and 5, it is more informative to present the real images instead of the binary masks.

3. In line 192 the authors explained one of their quality control tests, it would be good to mention that it is performed 6 days post-plating. As for now, the only indication is in Fig1d.

4. In Figure 1: it is not clear that the staining is performed at DIV21. Swapping panels c and d would probably improve readability? Why panel g shows the dispersions of the data points, while panel e does not? The data are plotted as mean {plus minus} SEM, were the data tested for normality? It is not clear from the method section.

5. Please clarify: In line 267 there are listed 17 small molecules. However, in Figure 2 there are 20 molecules labeled, and the number of labeled molecules for the inhibitors family does not match with the text (e.g., 3 BET inhibitors in the text, but only two labeled).

6. It is not clear from the figures, nor the text in lines 305-320 that the experiments with and without astrocytes are done in parallel.

7. What is the size of the Speckles filter used for the synapse thresholding? The range of 1 to 6 pixels per synapse seems a bit broad, especially in the low-end (1-2 pxs) it might be prone to detect scatter noise. Did the authors try to evaluate how changing those parameters affects detection, and if so, please explain the choice of the declared parameters?

Reviewer #3 (Recommendations for the authors):

The present study provides a quantitative platform to count synapses in cultured human neurons derived from iPSCs. This platform was used to identify novel signaling pathways important for synapse formation.

To strengthen the impact of these findings the author should address the following points:

1) All the methodology was used to quantify a presynaptic marker and indeed the effect of BET was measured on presynaptic synapsin1. So it will be nice to show if BET treatment is able to increase the staining of a postsynaptic marker (Homer1 for example), if feasible.

2) The mRNA-seq analysis indicates that BET treatment increases the expression of some synaptic and non synaptic proteins. However, these specific genetic modifications should be confirmed also by WB analysis of some of the identified major proteins.
