# Peer review - Round 1

Editors:
- Brandon K Harvey, NIDA/NIH United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60223.sa1](https://doi.org/10.7554/eLife.60223.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript by Kalinski et al. uses a combination of approaches including flow cytometry, scRNA-sequencing, parabiosis and transgenic reporter mice to characterize the immune cells at the site of an injured nerve. The study provides insight into the preparatory contributions of inflammation towards the regeneration of injured nerve tissue. Different populations of immune cells are shown to differentially populate regions of the injured nerve supporting the idea that GM-CSF signaling in the injured peripheral nerve is necessary for axon regeneration in spinal column after a conditioning lesion.

Decision letter after peer review:

Thank you for submitting your article "Sciatic Nerve Injury Triggered Inflammation, Insights into Conditioning-Lesion Induced Axon Regeneration" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Satyajit Rath as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alyson Fournier (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

Kalinski et al. use a combination of approaches including flow cytometry, scRNA-sequencing, parabiosis and transgenic reporter mice to characterize immune cells in the injured sciatic nerve and DRG. The study examines mechanisms by which inflammation helps to condition tissue for regeneration. They identify different populations of immune cells which differentially populate regions of the injured nerve and provide support for the idea that GM-CSF signaling in the injured sciatic nerve is necessary for spinal column axon regeneration after a conditioning lesion. All of the reviewers noted the abundance of data collected and that the data was technically sound overall, however, several concerns were raised regarding the presentation and description of results.

Essential revisions:

1) The major issue with the manuscript is that the presentation and description of results is unwieldy and is relatively inaccessible to the reader as presented. The extensive molecular detail and the inclusion of discussion points that should be relegated to the Discussion section. This is best exemplified for the presentation of results in Figure 5 and Figure 6. The text should be less descriptive and more explanatory similar to how it is written in the last paragraph of the subsection “The cellular landscape of injured peripheral nerve tissue”. The title also suggests that the inflammation that is triggered by crush injury should give insights into conditioning-lesion induced axon regeneration. However, the manuscript seems to consist of two independent stories. The descriptive parts on: “the cellular landscape…”, “the immune compartment…” and “the cell type specific expression of engulfment…” are very elaborate. Because these parts are so detailed, it is not connected to the rest of the story anymore and it seems to be an independent “storyline”. It would likely create a better reading flow if the descriptive part on the single cell RNA sequencing data is reduced to a minimum.

2) The scRNAseq data provides transcriptomic information of the whole nerve on day 3 after crush injury. As mentioned in the subsection “The cellular landscape of injured peripheral nerve tissue”, injury induced expansion of the immune compartment peaks around d3 when analyzed by flow cytometry. However, to be able to properly identify the corresponding transcriptomic changes in the immune compartment it would be better to include a dataset of scRNAseq of naive uninjured peripheral nerves. This could be either own experimental data or published data from one of the three recent scRNA-seq studies of murine peripheral nerves.

3) Figure 2A – Iba1 and F4/80 expression is stated to be maximal at 3 days post-injury based on fluorescence microscopy. However, the background staining for both red and green channels appears to be higher for days 1-7 post-SNC when compared to sham. The staining appears more intense in days 1-7 post-crush relative to control, but perhaps a more robust quantification of the images with a correction for the differences in background staining between sections is needed. Moreover, an issue of tissue integrity or folding in the section used for day 3 post-crush may be creating an artifact in top left of image due irregularities in the tissue. The intense overlap in the signal for all three channels supports this concern. If possible, a different section from this group that does not possess this issue should be examined. Alternatively, higher resolution images may be used to verify that distinct cellular structures are stained.

4) In Figure 9F the image magnifications appear to differ. Were the representative images of WT taken at the same magnification as the CSF2-/- mice since the apparent somatic size of WT is smaller than that of CSF2-/- based on their NF-H fluorescence staining? This would then require correction of the subsequent neurite length quantification on panel G. If the images were indeed taken at the same magnification, do the size of the somas significantly differ between two conditions.

5) Although the finding that GM-CSF is required for conditioning lesion induced axonal regeneration is exciting, the data acquired with the Csf2 KO mice is very minimal compared to the detailed analysis of the injured sciatic nerve. The mouse line induces a global knockout of GM-CSF, which provides a limitation to the interpretation of the data. This limitation should be emphasized further.

6) In the scRNA-seq dataset several mesenchymal clusters are identified. How was endoneurial vs. perineurial MES distinguished as claimed in the text. The location of these sub-clusters should be underlined by supporting evidence from literature references or by in situ visualization. Otherwise the statement should be adjusted.

7) Why was Erk1/2 used for normalization when analyzing the CD11b signal by W. Blot to corroborate the FACS data since the expression of ERK is affected by sciatic nerve injury?

8) Statistical: For the quantitative analysis of immune profiles in the deafferent DRG, the n numbers are not consistent. It is not possible to do a solid statistical test on n=3 vs. n=12 or n=14 so please increase the n for d1 and d3. For an unpaired t-test, the groups should have equal variance. When comparing more than 2 groups a one way ANOVA should be used. Please check your statistical testing for figures that include bar graphs with more than 2 groups (so naive-d1-d3-d7). When mentioning average or median values in the text, please add SD or SEM (in the subsection “The cellular landscape of injured peripheral nerve tissue”, for example).
