# Peer review - Round 1

Editors:
- Christian R Landry, Université Laval Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.53810.sa1](https://doi.org/10.7554/eLife.53810.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The authors performed a mutational scanning experiment of Hsp90, a large heat-shock protein involved in regulating multiple cellular processes. They mutated all positions of this large protein to other amino acids and measured the growth of each mutant in standard condition and five stress conditions that may require Hsp90's function. The authors found that many variants are deleterious, as expected, and that these cluster in specific regions and tend not to be found in Hsp90 orthologs. The authors found that some mutations are beneficial, but these tend to be condition-specific, suggesting that evolution in fluctuating environments would favor overall robustness rather than allele variants that would be beneficial in specific conditions. This study reports one of the most extensive genotype-fitness maps of a protein performed to date and brings novel hypotheses regarding the evolution of proteins that have a large array of molecular functions and binding partners.

Decision letter after peer review:

Thank you for submitting your article "Comprehensive fitness maps of Hsp90 show widespread environmental dependence" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Flynn et al., carried out a comprehensive deep mutational scanning of HSP90 in S cerevisiae (709 amino acids long). They measure the fitness effects of all possible single mutations and find that these effects are condition dependent. Their results allow to propose further models on the evolution of proteins such as HSP90 that play a role in stress response in variable environments. Overall, the study is elegantly designed, and the results are well presented. The three reviewers found the results highly interesting and found the scale of the experiments impressive. However, they raised several major points that need to be addressed. Some of them relate to the technical aspects of the work, others to the data analysis and finally, some relate to the potential broader impact of the results and interpretation.

The major comments are combined in a single list here:

1) The analysis of variability in the mutational sensitivity of synonymous mutations (discussed in subsection "Hsp90 potential for adaptation to environmental stress") seems a bit reductive. The analysis does not include the comparison of synonymous mutations at the beginning of the gene with the rest of synonymous mutations. The authors could have shown position-wise selection coefficients of synonymous mutations in a figure just to give a context of the data. In order to provide sense of the scale of variation, variability in synonymous mutations could be compared with that of non-synonymous mutations. Apart from this, there seems to be some inconsistent deleteriousness of some of the synonymous mutations (mentioned in subsection "Determination of Selection Coefficient"). I think it should be acknowledged in the results.

2) Figure 5—figure supplement 4B,C: statistical tests would be needed to draw a conclusion from the data.

3) Analysis of stop mutations

Similar to variability in the selection coefficients of the synonymous mutations, evidently there is also an extent of variability in the selection coefficients of stop mutations too (as seen in Figure 2—figure supplement 7). In my opinion, this aspect should have been addressed in the results. Also, are there any factors that determine the variability in the selection coefficients of stop mutations, apart from the position of the stop mutation?

4) Estimation of the level of between-replicate variation of deleterious mutations as a function of depth of sequencing. In the Results section, the authors acknowledge that the between-replicate variation is larger for the most deleterious mutations. As deleterious mutations are central to the results of this study, I think this point needs to be substantiated. In order to do so, an estimation of the level of between-replicate variation of deleterious mutations as a function of depth of sequencing could be shown.

5) Network analysis of altered protein-protein interactions

One of the most striking results of the study was that the beneficial mutations in elevated temperature condition and in case of diamide stress were found to be preferentially located on the binding surfaces of HSP90. However, the analysis to uncover the cause of such effect seems underdeveloped. Are there ways with which this could be considered further? Computationally, based on the mutationally altered binding between the protein interfaces, it could be possible to simulate the network rewiring and deduce the causes of the beneficial effect. Although not mandatory, such analyses would help in providing a network context to the study.

6) Relative strengths of the constraints. At various places in the text, the authors have analysed different constraints that guide mutational fitness effects while considering subsets of positions eg. ATP binding region, buried residues etc. However, I believe it could be helpful to analyse such strengths of constraints at the whole protein level. The estimation the relative strengths of the constraints and then ranking the constraints based on their strengths could be helpful in comparing the features of mutational sensitivity of HSP90 with other proteins such as with gentamicin-resistant gene in bacteria that they cite (Dandage et al., 2018). Such analysis could help in identifying the potentially unique features that are specific to HSP90.

7) Position-wise clustering of the variants

Figure 4B and Figure 5B: The analysis shown is difficult to understand. Either modifications in the plot or the caption is needed. The significance of the difference should be tested with a statistical test. How are the 'independent expectations' calculated?

8) The paralog of HSP90 is not discussed in the text. However, an earlier study showed that (https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1000347) one paralog is induced in expression when the other paralog is deleted (Figure 2, Hsp82). This seems to be a potential confounding factor if some mutations reduce protein abundance and in response the other copy's expression is induced. This may make some mutations be buffered by the other copy and not others. The strain used in this study appears to be the one described previously (Jiang et al., 2013) as a Hsc82 knockout. Therefore, interpretation of the fitness effects of Hsp82 variants is confounded by the absence of Hsc82. In nature, it is possible/likely that redundancy of the Hsp90 paralogs enables Hsp82 to navigate areas of the fitness landscape that appear selectively inaccessible in the present study (although there is now evidence that these paralogs exhibit some functional differences (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6689086/)). Relaxed constraint could on influence molecular evolution of Hsp90, specifically in regions that bind to clients and/or co-chaperones.

In addition, given the artificial context in which the protein is expressed, it seems likely that this system fails to recapitulate the native transcriptional, post-transcriptional, or translational regulation of the native system. While I do not doubt that the authors have devised an elegant system for assessing the effect of the various mutants on the Hsp90 protein (and in some cases the relevant mRNA, in the case of meaningfully important synonyms), it seems likely that the native gene(s) are under a much more complex selective pressure. I understand that fully addressing this concern experimentally is likely beyond the scope of the current study, but it needs to be considered in the Discussion section.

9) Another major point relates to expression levels (Hsp82 as stated in subsection "Impact of stress conditions on mutational sensitivity of Hsp90"). Was expression of Hsp82 affected by the stress conditions? The manuscript references a previous paper that describes a 10-fold reduction in Hsp82 expression, presumably in standard conditions. Is Hsp82 downregulated to a similar in the stress conditions? I would want to see Hsp82 expression levels before drawing any conclusions about Hsp82 function in the stress conditions. Another issue relates to the protein. What is the half-life of HSP90 and what happens when transcription is shut off?

10) Other technical aspects would be to be better described. For instance, the copy number and auxotrophy of the Hsp90 mutant expression plasmid are not indicated. Moreover, the genetic background of the experimental strains are also insufficiently described. Other questions also arise when trying to make sense of the experimental details. Which paralog is deleted and which is under the control of the galactose-inducible promoter? How many technical replicates per environment? I think duplicates for the standard condition and none for the other selective conditions? But this was hard to tell. How does noise affect the estimation of selective coefficients? Are the authors convinced that the behavior of this promoter is consistent across stress conditions? I would also like to know the copy number of plasmids used for cloning and expressing the libraries.

11) Another concern is regarding the scope and broad interest of the work described in the manuscript. The core experiment appears well designed and carefully conducted, but most of the key findings are intuitive or reflect existing knowledge of the Hsp90 protein or its intermolecular interactions. For reasons related to the three concerns described in more detail below, the strongest claims pertaining to evolution and selection are perhaps not best-addressed in this model system. Rather, it seems most suited for examining the behavior and function of the Hsp90 polypeptide in the abstract, and the findings here may be of interest to a more focused audience. Finally, there is limited validation, confirmation, or exploration of the findings from the selection experiment in orthogonal experimental systems.

12) One of the major novelties of the work is the systematic assessment of GXE. Since only a few studies have performed such comprehensive assays, it would be important to mention them and contrast them with the current work. I missed a comparison and discussion, or even just a mention, of the fitness landscapes of 23,000 tRNA genotypes across four different selective environments (Li and Zhang, 2018). In that paper, whereas the GxE was pervasive, the patterns detected were so simple that the fitness landscape in a given environment could be easily predicted from the fitness of a few genotypes in another environment using a piecewise linear regression model. Would the same approach work here? If that approach does not work with the Hsp90 data, could that indicate a fundamental difference in fitness landscapes and GxE interactions between RNA molecules and proteins?

13) My final significant question relates to the observation of minimal antagonistic pleiotropy (and little deleterious variation) amongst naturally occurring variants across different experimental conditions. The authors claim that this constitutes evidence for selection on "robustness" across fluctuating environments. I would propose that, rather, it may suggest that the molecular function (potentially modulo selective client binding, as the authors observe) is simply similar across environments and thus, "robustness" merely reflects that Hsp90 foldase function is an important cellular process (as reflected by the inviability of the HSP82 HSC82 double-deletion strain). Indeed, it seems most "essential" genes would likely exhibit this behavior by dint of the importance of maintaining their function. Perhaps this is a semantic difference; in any case the authors would do well to clarify this line of argument in the text.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Comprehensive fitness maps of Hsp90 show widespread environmental dependence" for further consideration by eLife. Your revised article has been evaluated by Patricia Wittkopp (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

1) The randomizations discussed in subsection "Constraint of mutational sensitivity at high temperature" should be described in the Materials and methods section.

2) The description of the different types of mutations in subsection "Constraint of mutational sensitivity at high temperature" could be better explained. Deleterious mutations are not always purged so it would be better to say "strongly deleterious mutations that are purged" to contrast with slightly deleterious ones (nearly-neutral).

3) The Western blot shown in Figure 6—figure supplement 1 does not include a loading control to show that the same amount of protein was loaded. If the amount of protein loaded was measured and normalized, please specify how otherwise it would be important to mention how you can compare the samples without appropriate controls.

4) It would be better to show the data mentioned here: "cells containing a null-rescue plasmid had stopped growing and Hsp90 was undetectable by Western blot (data not shown)."

5) The tabulated data used to generate figures is provided but the code used to generate this data is not provided. Please provide the code or make it available through an online public repositories such as GitHub or others.
