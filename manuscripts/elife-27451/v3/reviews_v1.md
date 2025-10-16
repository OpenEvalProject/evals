# Peer review - Round 1

Editors:
- Antoine M van Oijen, University of Wollongong Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.27451.029](https://doi.org/10.7554/eLife.27451.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Transcription factor clusters regulate genes in eukaryotic cells" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Jessica Tyler as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Serge Pelet (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

In this article, the authors present a detailed analysis of the dynamics of MIG1, a transcription factor that plays a key role in glucose sensing in yeast. Using a combination of live-cell single-molecule tracking, bioinformatics analysis, and in vitro assays, they unveil a MIG1 clustering mechanisms involved in the response to glucose. In recent years, partly thanks to single-molecule tools, the role of transcription-factor clustering in transcriptional regulation has become an important topic of study. The present work adds to this growing list and in particular identifies a clustering mechanism through the depletion forces and via disordered domains of the protein. The manuscript is clearly written and the results will be of interest to the community. However, before publication is considered, a number of concerns will need to be addressed in relation to quantification, statistics, and controls.

Essential revisions:

It is not clear how the stoichiometry of molecules within a single focus was determined. The authors mention the measurement of single GFP photobleaching (Results paragraph three), but don't show any data. The manuscript will have to include raw trajectories and their analysis, showing the intensity distributions for single GFP bleaching steps measured intracellularly. Without these data, none of the conclusions are supported.

The authors confirm the formation of clusters by performing in vitro experiments under conditions that mimic intracellular crowding. The same focus tracking analysis is used as in the in vivo experiments. However, no raw imaging data is provided to visually confirm focus formation

The quantified data of nuclear and cytoplasmic enrichment presented in Figure 1B don't seem to match the image of the single cell. According to the image (and data from Bendrioua et al., 2014), Mig1 accumulates and remains in the nucleus for at least 400s. While the quantification reveals a drop in Mig1 nuclear level and an enrichment in Mig1 cytoplasmic level after 200 ms. Also after the switch to glucose (-) no sharp drop in nuclear level is observed in the quantified curve as expected from the image and previous quantifications (Bendrioua et al., 2014).

According to the data in Table 2, there is an increase in total fluorescence level going from the glucose (+) to the glucose (-) conditions for Mig1 and Msn2. Can these changes be due to an expression of the protein? How long after the switch to the low C-source medium are these values quantified? In addition, it has been reported that GFP is sensitive to pH and pH changes upon glucose starvation (Roberts et al., Sci. Rep. 2016). Have the authors experienced any difference in GFP brightness between conditions?

The Zn finger mutation of Mig1 seems an interesting control for many of the experiments performed. This strain is however not included in the strain list. Since the author claim that nuclear accumulation is governed by retention in the nucleus due to the binding of DNA. The ZF∆ mutant would be a good control. The overlap between Mig1 dots and PP7 foci should also disappear in this mutant.

In Figure 3B, the authors present data on the constrained diffusion of the foci due to nuclear anchoring of Mig1. If I understood properly, the deviation form the dashed line represents the constrained diffusion. However, I don't see a noticeable difference between the deviation observed for small or large foci or even cytoplasmic ones. Therefore I don't understand how this can be interpreted as a effect of the DNA anchoring of the Mig1 clusters. Again a ZF∆ Mig1 would be an interesting control to measure.

The authors present data on the in vitro oligomerisation of Mig1-GFP triggered by PEG addition. As a control, they use mGFP alone. First of all, this control should be performed with the same fluorescent protein for the TF bound and the GFP alone experiment. In addition, the number of measured fluorescent dots has to be the same in both cases. However 1000 dots where measured for the Mig1-GFP versus 100 for the GFP. Since the high stoichiometry clusters are found with <1% probability, the chance of observing a single high stoichiometry cluster is lower than 1 for the control experiment.

I'm not a specialist of electron microscopy, however I find a few elements in this experiment puzzling. The authors state that they measured 150 cells and only in 10 of them did they see a cluster of Mig1 or Msn2. How many untagged cells did they measure to make sure that this phenomena is not present in untagged strains? Why don't we see individual Mig1 or Msn2 molecules labels with the gold particles in these images. Also no data of Mig1 nuclear cluster has been obtained. These low statistics makes me wonder about the quality of this dataset.
