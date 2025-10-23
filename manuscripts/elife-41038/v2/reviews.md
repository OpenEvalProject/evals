# Peer review - Round 1

Editors:
- Daniel J Kliebenstein, University of California, Davis United States

Reviewers:
- Arthur Korte, Vienna Biocenter Austria

## Review text

DOI: [10.7554/eLife.41038.020](https://doi.org/10.7554/eLife.41038.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Drought adaptation in Arabidopsis thaliana by extensive genetic loss-of-function" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Christian Hardtke as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript identifies a subset of existing natural knockouts and provides evidence that they are likely causal in natural variation within the species.

Essential revisions:

1) There was a concern that the inflated GWAS significance may be a result of some consistent error imparted by the functional allele assignment rather than all the genes being causal. Some analysis that can argue against this would be helpful especially to convince the generalist reviewer. We came up with two ideas but are willing to assess any other test you can develop. The ideas raised in our discussion were a) permute the phenotype to see that after this the glm will not lead to inflated results or b) permute the respective binary gene-wise score to see that an arbitrary assignment with the same allele frequency will agree with the null hypothesis.

2) The eco/eco aspects of the events needs to be assessed more broadly given the breadth of Arabidopsis life styles and how positive in one may be negative in another.

3) There is a need to better discuss the calling of specific events as a number of known events were not found.

Reviewer #1:

The authors conduct a survey to find LOF mutations with regards to the Col-0 reference genome. They then work to show that there is an association to potential adaptation and drought. This is a highly interesting manuscript but there are some issues with false negative rates in the LOF lists and referencing of the primary literature.

One conflict in this manuscript that I had was the idea that the whole manuscript was about drought adaptation yet the validation was on flowering time. There was no real discussion on if these mutants may or may not alter drought responses and if so, are those effects as unidirectional as for flowering. This conflict would optimally be resolved with experimental data at best or alternatively with discussion reflecting this difficulty.

I find it odd that none of the citations for LOF mutations contributing to adaptation or fitness are prior to 2006 even though there are a large number of Arabidopsis and other mutations that had LOF natural variation found prior to that. This includes key genes controlling flowering and defense such as RPM1, RPS2, FLM, AOP2, etc. Some of these genes such as the work by Bergelson on R genes and Kliebenstein on glucosinolates have direct evidence of field fitness effects of these natural variants in LOF. I understand that the authors prefer to use review articles but they should really use primary research literature as that is the real work that should be given acknowledgement especially as there is no length limit in eLife. This lack of primary literature may have led to the next issue about the LOF gene list.

A cursory analysis of the list of genes in the supplementary information found that the list is missing a number of genes with published loss of function events, I.e. BRX, AOP2, MAM, etc. This indicates that there is a significant false negative issue within the compilation of genes. The authors need to go through the literature to identify a collection of genes with known loss-of-function events and then assess how many they did or did not find. This is essential to let future researchers know how complete the list of genes is or is not. Is it possible that this is biased by use of the Col-0 genome as the reference and potentially not looking for GOF alleles in the other accessions which would be LOF if you shift the reference genome?

Equally, it seems like the authors should discuss settings where the LOF are not multiple independent events as is the case for RPM1 and RPS2. The general text has a feeling that all LOF are multiple independent events which may come from the soft sweep citation but that is not the exclusive view for plant natural variation.

Flowering time analysis seems to have only been conducted in one environment. The authors should discuss the fact that the environment has a key role in determining flowering time and how doing a broader range of environments with the mutants may influence the results.

For Figure 3F, is a linear correlation the best fit to the data? It looks like a non-linear correlation would be a better fit. The authors should do a model comparison of linear and non-linear regressions to see which best fits the data as a non-linear fit could alter the interpretation as that would suggest a maximal effect.

Reviewer #2:

This comprehensive study integrates across diverse approaches to detect drought timing and evaluate the genetic basis of adaptation to drought in the context of loss of function in the model organism, Arabidopsis thaliana. The innovative use of the Vegetative Health Index generated data on the timing of drought for numerous accessions of Arabidopsis. This approach could potentially be applied to other systems. The current study uses previously published genomic data to detect potential candidate genes associated with drought (as measured via the VHI) and flowering time (from a previously published growth chamber experiment). After evaluating statistical associations between drought, loss of function genes, and flowering time, the authors conducted gene knock out studies at several candidate genes showing relationships between loss of function and spring drought to evaluate causal link with flowering time.

I wonder about the adaptive nature of these associations. For example, is delayed flowering adaptive under spring drought and earlier flowering adaptive under summer drought? That is, are loss of function alleles associated with adaptive changes in flowering phenology? In the third paragraph of the Results and Discussion, the authors point to two studies (Kooyers, 2015; and Dittberner, 2018) to support the assertion that these phonological changes are adaptive. Unfortunately, the Dittberner Endnote citation was inadvertently excluded from the references, so that I cannot look at it. Kooyers, 2015, discusses drought avoidance vs. escape as general plant strategies, with escape associated with rapid growth and avoidance associated with other morphological and physiological traits that confer higher water-use efficiency. The typical thought is that plants can escape from drought by flowering early. In the current study, the authors suggest that later flowering genotypes may avoid spring drought. When does germination occur in sites with spring drought? Late flowering genotypes would still experience the spring drought as juveniles, depending on when germination occurred. It does not seem clear that delay flowering enables those plants to escape from the drought, given that early life history stages are very susceptible to drought. It seems problematic to refer to loss of function as generating adaptive shifts in flowering phenology without fitness data (ideally in the field) to test those hypotheses directly. That said, I appreciate that the Dn/Ds and Pn/Ps analyses point to positive selection for loss of function alleles in genes associated with drought or flowering time.

Figure 1A: What data are used to determine the regions of drought stress (in graded brown at the bottom of the top two panels)? The Materials and methods (subsection “Satellite-Detected Drought Histories of Arabidopsis”, first paragraph) set 40 as the threshold for drought (values of HVI <40 are indicative of drought). How was that value determined? How does it relate to drought stress as perceived or experienced by Arabidopsis in nature? The authors use the HVI to determine the timing of drought for Arabidopsis. Have they ground-truthed these drought metrics in any of the field sites? How reliable is the HVI for characterizing exposure of Arabidopsis to drought in its native range?

Figure 1C focuses on spring vs. summer droughts. Have winter droughts (present in panel 1B, right side) affected the timing of flowering of Arabidopsis in any of these populations? It seems like winter drought could affect flowering time for both fall germinating and spring germinating ecotypes.

What other factors could drive population divergence between populations with spring vs. summer drought? The manuscript seems to assume that drought is the only factor affecting those differences. For example, the Materials and methods state "Summer drought genes were identified as those in which LoF alleles are found in ecotypes that experience a significantly (βdrought timing <0 & Pdrought timing <0.05) more negative drought-timing index […] Conversely, spring drought genes were identified as those in which LoF alleles are found in ecotypes that experience a significantly (βdrought timing > 0 & Pdrought timing <0.05) more positive drought-timing index…" Are there other environmental factors that covary with drought that could also influence evolution at these loci? How can the authors be sure that these are really "summer drought" vs. "spring drought" genes? Are these genes consistent with mapped regions for drought tolerance in Arabidopsis?

Additional points:

I recommend deleting the first part of the sentence ("Plants have been adapting to drought for millennia.…"). For one, plants have been adapting to drought ever since they colonized land from the mid-Ordovician to the Devonian, over 400 million years ago. Secondly, this phrase does not provide information that advances the narrative.

Introduction, second paragraph: Please provide citations for the statement that most research has focused on late-season droughts. This statement does not resonate with my experience conducting studies and reviewing manuscripts. When possible to manipulate in the field, researchers impose drought in an ecologically-relevant fashion. In the lab, researchers generally time drought treatments for a developmentally-relevant stage.

Figure 1A It might be useful to label the two locations with the names of the Arabidopsis accessions or provide the geographic region, in addition to the latitudes and longitude.

Both panels of Figure 1A (especially the panel on the right) seem to imply that drought stress is occurring less frequently through time. The darker lines indicative of more recent years seem to occur in regions of higher VHI. Is that correct?

In the subsection “Experimental Testing of Predicted Phenotypes in Gene Knockout Lines”, it states that flowering time was assessed as days from planting to the emergence of the first flower. Is there variation in germination timing? Why not measure flowering time as days from germination to the first flower?

Figure 3F: Is this relationship linear or might a curvilinear model fit better?

Reviewer #3:

Monroe and colleagues describe the link of loss-of-function Alleles with drought adaptation and flowering time in A. thaliana. The manuscript is well written and interesting conclusions are reported. Especially the high overlap of associations for summer drought and early flowering and spring drought and late flowering is intriguing. Additional the functional follow-up in T-DNA knock out lines is excellent.

Still, I have one major comment.

My major concern is the statistical framework used for GWAS.

The authors used logistic regression in a glm and added the first 3 principle components to correct for population structure. This differs from the standard GWAS procedure in A. thaliana which uses a linear mixed model to correct for population structure confounding. The rational why the authors used this model is not well described in the manuscript. Additionally, the results differ markedly from the analysis with a classical LMM. (I run a normal LMM with the provided data for comparison, happy to provide this if needed) Next, the qq_plot is also highly inflated (which might be expected collapsing LoF Alleles to one score per gene), but is not if a normal LMM is used.

To summarize, I am not completely sure what to make out of this, especially as the results and conclusion look really nice with the presented method (e.g. Figure 2 is really impressive).

Still, it would be good if the authors at least comment on why to use the proposed framework and the inflation observed in a qq_plot.
