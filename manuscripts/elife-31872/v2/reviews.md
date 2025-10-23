# Peer review - Round 1

Editors:
- Emmanuel Levy, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31872.026](https://doi.org/10.7554/eLife.31872.026)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Patterns of protein subcellular localization change inferred by integrating 100,000s of images from microscopy screens" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Emmanuel Levy as a Reviewing Editor and Naama Barkai as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another, and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Lu et al. introduce the concept of "localization profile" representing a protein's localization signature across multiple environmental conditions. The use of protein profiles has proved powerful as an approach to study protein function as well as to characterize functional relationships between proteins. It has been employed in numerous contexts and includes, for example, phylogenetic, mRNA expression, physical interactions or genetic interaction profiles.

Here, the authors characterize protein localization profiles using images from several proteome–wide fluorescence microscopy screens of the yeast GFP library. Inferring protein localization from microscopy images normally involves human intervention to train classifiers that are hardly generalizable. As a result, it has been difficult to carry out systematic and quantitative comparisons of protein localization across multiple screens carried out at different times or involving different physiological conditions. To overcome this difficulty, the authors employed an unsupervised approach to analyzing protein localization, which they applied to several proteome–wide microscopy screens.

The localization features measured across conditions formed protein localization signatures, which the authors clustered to identify groups of similarly behaved proteins. Clusters showed enrichment for functionally related proteins. Numerous changes detected were validated by known literature, and novel changes were observed. Most of the clusters of proteins with similar signature in localization–change were not associated to similar transcriptional regulation nor were they enriched for physically interacting proteins.

Essential revisions:

Globally, all reviewers found that the method shows an important potential. Numerous comments point to analyses needing to be more thorough, sometimes requiring a more systematic examination. Considering that the data underlying the kinase deletions appear to be of lower quality, I suggest cutting that part. Figures are often hard to follow, so particular attention needs to be given to the presentation of the results. Please find below a consolidated list of the reviewer's comments.

1) The authors indicate they derive descriptors even when a single cell is available. Was this decision taken based on a general optimization scheme or is it arbitrary? What fraction of the data corresponds to 1 to 5 cells? One should show that this decision brings more signal than noise.

2) A significant fraction of strains in the GFP library show fluorescence levels that are close to auto–fluorescence, and in that respect can be hard to analyze. How do such strains affect this work? What fraction of the strains in the matrix of Figure 1 are in the "top–50% abundance class?"

3) More generally, to what extent does profile similarity depend on signal intensity or protein abundance?

4) How was the number of features decided upon? Each feature described in Figure S1 has 10 pixels associated with it (and therefore I assume 10 parameters). Why are 10 features necessary when, e.g., considering "distance to the cell edge." Could one feature, or perhaps an average of the features facilitate interpretation while being equally informative in the profile comparison? It would be necessary to establish an objective criterion that can be optimized – such as "number of changes detected across different conditions versus across replicates of the same condition." (this objective criterion can also be used to set the minimum number of cells to be used, see point #1.). A detailed depiction of the features employed is needed.

5) The approach is validated using a set of 20 pictures, which may not account for global effects. A more general benchmark would, therefore, make sense in that respect too (see comment #4).

6) In the validation, the authors infer a false positive rate of ~50%. They should provide a sense of what the origin of these false positives is, and how it may impact the conclusions. For example, that proteins in the same clusters to not exhibit similar transcription profile, physical interactions, or localization.

7) An analysis of a limited number of clusters is presented in Table 1, where GO enrichment is carried out. Are these the only clusters showing functional enrichment? The global nature of this work begs for a more general analysis of GO enrichment, i.e., by defining clusters across the entire matrix and analyzing GO enrichment for all of them, not a handful only. Even if a few are described in Table 1, the results can be provided as Supplementary data. In addition, "numbers" can be added to Table 1 (number of proteins in the cluster and number corresponding to the annotation being enriched).

8) Figure 4C contains cells that do not appear to contain any green fluorescence, while others show a strong signal. Such bimodal behavior is worrying as it may not be biological. Perhaps that some cells have lost their fluorescence during the SGA process for example. Is the localization profile affected by such cases? Is such bimodal behavior widespread? If so it should be accounted for in the analyses, and such cases would need to be filtered or flagged.

9) Global "quality control" figures should be shown, suggestions for this are given below:

– Subsection “An unsupervised analysis of protein localization changes in over 280,000 images”: More details should be presented regarding this sentence. Can a distribution of "localization change" score be shown for replicates of the same condition and different conditions? More of such "sanity check" plots would help get a better sense of how the method is doing. (See comment #1)

– The consistency of protein abundance (or rank abundance) across the different screen should be controlled.

– The association between change in localization, expression–change, and PPIs is shown in Figure 6 for a few cases, but it would be more valuable to show it in a systematic fashion, for example by showing (i) how Z–score for profile change in the data from Figure 1 correlate with a Z–score for abundance change, or (ii) How profile similarity relates to other measures of functional relatedness? E.g., protein interaction profile similarity, genetic interaction profile similarity, expression–profile similarity, etc. Such a bird's eye view of the data is lacking and would add much to this work.

– The last analysis suggests that proteins with different localizations can exhibit a similar change. This is counter–intuitive, and more data could be provided to examine the origin of such cases

– Looking at Figure 6C, why is cluster I, which contains ribosomal proteins, not enriched in physical interactions? If using BioGrid one does not need to limit oneself to low–throughput data. A large and high–quality dataset can be obtained by taking all physical interactions supported by more than one PMID. Lastly, the "clusters circles" of Figure 6C do not overlay with points.

10) The authors identified Rtg3 to be a pulsing transcription factor through cluster analysis and conducted time–lapse movies to confirm such dynamics. In the cited reference (Dalal et al., 2014), pulsing was defined as TFs that exhibit dynamic shuttling between nucleus and cytoplasm during the steady–state response to added stresses. In Figure 3, the authors didn't indicate when the stress was added and whether the cells on average have reached steady–state. The authors didn't specify what stress condition each cell represent in Figure 3. Lastly, to analyze "longest pulse duration" (Figure 3C) does not provide a robust measure. The mean/median duration should be presented.

11) Analysis of protein level change. In Figure 6A, the authors compared localization pattern with microarray pattern. However, it would be more natural to compare the protein expression pattern with microarray pattern, and more importantly protein expression with localization changes. It is indeed always difficult to merge different data from different laboratories, but protein expression is readily available from the images as the sum of GFP intensities in the cell.
