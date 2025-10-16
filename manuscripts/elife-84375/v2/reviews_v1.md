# Peer review - Round 1

Editors:
- Paul W Noble, https://ror.org/02pammg90 Cedars-Sinai Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84375.sa0](https://doi.org/10.7554/eLife.84375.sa0)

The study addresses a significant impediment to deriving maximal value from living tissue culture systems, which is simultaneously distinguishing and mapping the activity of multiple constituent cell types over the course of experimental perturbations. The authors present a label-free approach that involves collecting autofluorescence and morphological features that provide distinct signatures for mouse tracheal epithelium and demonstrate its application for live imaging of secretory cells. This platform may be very valuable for answering specific experimental questions about tracheal cell behavior in disease.


---

# Peer review - Round 1

Editors:
- Paul W Noble, https://ror.org/02pammg90 Cedars-Sinai Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84375.sa1](https://doi.org/10.7554/eLife.84375.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Label free autofluorescence imaging permits comprehensive and simultaneous assignment of cell type identity and reveals the existence of airway secretory cell associated antigen passages (SAPs)" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Paul Noble as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Both reviewers find great merit in the interesting study. However, they both raise important issues that we would like the authors to address below:

A) Reproducibility:

– Figure 3E, list how many cells were measured in each instance.

– Figure 3F unclear from figure or legend what dimension reduction algorithm was used (PCA? Other?).

– Figure 3 Suppl 2 is not useful as authors don't analyze subsets, any data can form new clusters based on the method used.

– Code should ideally be shared in Github, or in a containerized format in supplement, or anything other than in a PDF file.

B) Minimalism:

– Can the same be achieved just with morphological characteristics? (w/o FAD/NAD(P)H). Using your already existing data, repeat classification analysis omitting the ratios, and show the effect on accuracy/clustering.

– Alternatively, figure 3E: Show which features contribute most to detection in each case. E.g.: Secretory cells' low ratio, ciliated vs ionocyte YZ aspect, etc.

C) Generalizability:

– Describe in conclusions the conditions in which you predict that the method may need to be re-optimized (e.g. inflammation, infection, others) due to metabolic changes.

– Change P3L83: "autofluorescence signature under the conditions studied in this work can be used.."

– Relatedly, using your already existing data, is your ability to detect cell types maintained after Rotenone, Antimycin A, or FCCP? this would provide a clue as to the limitations. This loss of resolution is alluded to in P23L328 although not clear how much this is affected.

D) SAPs:

– Using your already existing data, quantify what proportion of secretory cells show the "SAP-like" empty structures at baseline.

– Figure 5C put times in figure (1, 9, 31, 40, 53, 60 minutes).

– Supplemental video: add a timescale.

– The methacholine time course should be improved by quantification of more instances of secretion, and by including appropriate controls:

– Compare SAP formation in absence of methacholine stimulation. Epithelia are very sensitive.

– How often do secretory cells take up and secrete FITC-dextran? This analysis does not need to be extensive as you are only claiming the "existence" of the SAPs, however, would be best to show more than one time only.

E) Others:

– Cite the preprint by coauthor Vinarsky (Kwok et al. 2022) when describing ex vivo prep.

– Cite Kretschmer et al. 2016 (airway-immune interaction, did not separate cell types).

– P2L50, unclear what authors refer to, reference Lin et al. is listed as "submitted" and not available, either remove mention or update citation.

– P23L321, "333% decrease in the CCSP" clarify, as absolute fluorescence value should not possibly decrease by more than 100%.

– Figure 5 confusing choice of colors as Tomato is shown as the same color as Draq5.

1) For the validation in Figure 2, it's not clear whether the cell type was identified by the autofluorescence and then confirmed by the immunostaining, or if and how "positive" and "negative" cells were inferred by autofluorescence. For instance, in Figure 2A, some cells are relatively bright in yellow fluorescence but negative for acetylated tubulin. If this is because the yellow fluorescence pseudocolor is only one feature of the ratiometric signature, that seems fine, but it would be useful to somehow demonstrate visually that the autofluorescence-based identification is independent of the immunostaining. It's just not clear if this is the case from the legend. Panel iii legend says it is an overlay of the staining and autofluorescence but to my eye, it looks like just the autofluorescence with a dotted line demarcating the cell boundaries.

2) Segmentation of single cells by autofluorescence looks excellent for ciliated and secretory cells but is less obvious for basal cells (Figure 2C). Was this done manually (drawing the dashed line) or is the workflow capable of performing this accurately independent of the immunostaining?

3) In Figure 3, it's difficult to get a sense of both of these issues (mentioned in 1 and 2) since in all of the panels A-D it is not easy to distinguish the "positive" cells or to segment the cell by eye based on the autofluorescence image shown.

4) The accuracy of cell type discrimination is quite good however it would be helpful to provide more details about how this was defined and performed. What was the "ground truth" for the cell type used to measure the accuracy? Did this involve immunostaining for cell-type markers?

5) It would be helpful to know how long mouse tracheal explants can be cultured with reasonable maintenance of the autofluorescence features.
