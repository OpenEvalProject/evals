# Peer review - Round 1

Editors:
- Frank LH Menke, The Sainsbury Laboratory United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.47864.sa1](https://doi.org/10.7554/eLife.47864.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Proximity labeling of protein complexes and cell type-specific organellar proteomes in Arabidopsis enabled by TurboID" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Christian Hardtke as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Mair et al., (Tools and Resources) has undertaken a robust assessment of an improved proximity labeling with biotin (BioID) approach in plants. Few studies in plants have employed BioID, and here the authors have presented a laborious collection of data outlining conditions necessary for the implementation of these improved methods (TurboID and miniTurboID) to identify new protein-protein interactions in plants in both stable and transient backgrounds. The authors start out by comparing cytosolic and nuclear localized BirA*- and TurboID- and MiniTurboID-YFP fusion expressed transiently in N. benthamiana and stably expressed in Arabidopsis transgenic lines. Using carefully designed experiments variables such as labelling temperature, biotin concentration, labelling time are tested and optimal conditions identified for TurboID as well as miniTurbo. This is done in N. benthamiana leaves as well as in different developmental stages and organs of Arabidopsis. Optimal conditions for affinity purification of biotinylated proteins and sample processing prior to mass spec analysis are carefully worked out and documented in great detail. Once these conditions are worked out the authors test the TurboID version to characterize a cell type specific transcription factor (FAMA) complex, with a FAMA-TurboID fusion, as well as the nuclear composition of specific guard cells expression transcription factor FAMA (pFAMA:TurboID). This is done in a temporal manor, by using short and medium length labelling times (0.5 and 3 hrs) compared to O hrs as well as comparison to the nuclear proteome (pUBQ:TurboID) and non-transformed negative controls. Both the FAMA complex and the FAMA nucleo-proteome experiments are very well designed and well documented. The FAMA complex experiment after filtering out 'non-specific' biotinylated proteins result in 47 potential FAMA complex associated/neighbourhood proteins.

The manuscript also describes a collection of vectors that have been made available for rapid implementation of their approach of this technique by the community.

Overall, performed experiments were well designed and presented data/information are very valuable for the plant science community to design the TurboID and miniTurbo based PL experiments for their researches.

Essential revisions:

1) Could the authors please explain how normalization of the data during MaxQuant search was done and/or was this done with Perseus? Some samples are very different from control samples, and in these cases application of global normalization across all samples during MaxQuant search (for instance) may bias the results significantly.

2) Please describe the filtering process and methods in more detail. The filtering process (Figure 5 and Figure 6) is difficult to really follow and does rely on numerous factors involved with MS data processing (matching parameters, LFQ parameters). The work has been replicated (n=3) which does add higher levels of certainty in the final results – FAMA interaction candidates and a guard cell nuclear proteome. But the initial datasets are 2511 and 3176 proteins, respectively and are filtered to 47 and 451/1583 proteins. For the GC proteome the authors indicate they found several known nuclear marker for young GCs – in fact they found 3 (subsection “Suitability of TurboID and miniTurboID for application in plants and performance of TurboID in FAMA-complex identification and nuclear proteome analysis”, last paragraph). It would be helpfull in understanding this extensive filtereing if authors could provide the MaxQuant Search files such as 'experimentalDesign', 'parameters' for the reviewers (and include in the Pride data submission).

3) The extensive data filtering to generate a high confidence sets (especially with regard to FAMA interactors) would usually require validation of some of the new candidates. Have the authors conducted any preliminary validations of the new interactors? Even relatively preliminary data would strengthen their claims for this approach. This could be preliminary transient work e.g. co express FAMA-TurboId and Target:Myc, pull down with streptavidin and conduct a western blot with anti-Myc. This would ideally be transient targets rather than complex partners, as this is the articulated advantage of this method over e.g. AP-MS.

4) The access to the raw MS data in PRIDE does not work. Both PRIDE login details resulted in no available data. I would guess data have been updated in the interim and this requires a new username / password to be issued for reviewers. Thus the robustness of the MS data matching employed by the authors could not be evaluated nor examine the quantitative process which is presumably available in a viewable data format.

5) Figure 5—figure supplement 2B: Why is replicate 1 is separated from replicate 2 and 3? It seems that separation by replicates is more significant than separation by genotypes. Is this due to how samples were processed? It was not totally clear from the method. Would be nice to have multi scatter plots as well to show correlation between samples.

6) In my understanding Branon et al. named the new ligases as TurboID(TbID) and miniTurbo(mTb), and therefore authors should use same terms to avoid any confusions.
