# Peer review - Round 1

Editors:
- Eduardo Eyras, Australian National University Australia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59629.sa1](https://doi.org/10.7554/eLife.59629.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This article describes a new method to re-examine the role of negative selection in cancer. The authors find new evidence of negative selection against inactivating somatic mutations, thus highlighting new mechanisms of tumor survival.

Decision letter after peer review:

Thank you for submitting your article "Use of signals of positive and negative selection to distinguish cancer genes and passenger genes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Patricia Wittkopp as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary

This work describes a novel approach to address the important and still open question of the extent of negative selection in cancer and the potential implications. The authors use data from the catalogue of somatic mutations (COSMIC) and a straightforward approach comparing synonymous, nonsynonymous and nonsense mutation counts to separate genes into Oncogenes, Tumor suppressors and Essential genes. The authors conclude that negative selection plays an important role during tumor evolution.

Essential revisions

Reviewers agreed that this work is timely and relevant, but also agreed that there are several important aspects that need revision/improvement before it can be accepted for publication in eLife.

Structure of the paper

1) The reviewers agreed that there are various aspects of the structure of the paper that require especial attention. The Introduction is a bit lengthy and very focused. It introduces different questions, e.g. hallmarks, prediction of oncogenes and tumor suppressors, prediction of selection, etc and it reads like multiple introductions to different articles. Many parts (e.g. the discussion of cancer hallmarks) could be shortened substantially, which would make it easier to read the paper. One suggestion is to mainly introduce the models of cancer evolution with respect to the SNVs and indels, and the different models and limitations in the estimation of negative selection in cancer and why it is difficult to detect, see e.g. (Zapata et al., 2018, Lopez et al., 2020, Tilk et al., 2019).

2) Additionally, it will be important to include citations to previous work on the detection of negative selection in cancer that has been omitted. For example, in paragraph five of “Carcinogenesis as an evolutionary process” they should add the work from (Zapata et al., 2018, Van den Eynden et al., 2017, Martincorena et al., 2017, Pyatnitskiy et al., 2015).

3) Both reviewers agreed that the Results section is repetitive and unbalanced with respect to the Materials and methods section. The work would benefit from streamlining the Results part and moving details to the Materials and methods section.

4) Regarding the Discussion, it is also very lengthy and lack focus. The authors should make clearer the main results and take-home messages from their work. At the moment, this is not very clear.

5) For simplicity and to improve readability of the manuscript, it was suggested that the authors focus on 2 standard deviation through the manuscript, instead of describing repetitively the results with 1SD and 2SD.

6) Regarding the presentation of the results, the reviewers suggested to redesign the figures in such a way that they describe the methodological approach, present the major results of their analysis, and show a comparison of these results with previous methods, and lastly (currently as a table) show the association between the identified genes and the hallmarks of cancer.

Comparisons with previous studies

7) One of the problems with the present work raised by the reviewers is that the authors did not performed sufficient comparisons of their results with previous studies. The authors used a seemingly simple approach to measure selection, dividing fractions of frequencies of different mutation classes by each other, with relatively arbitrary cutoffs, e.g. 1 or 2 standard deviations from the mean, to define gene sets. The manuscript does not show the advantages of this method over previous approaches. The authors should clearly show that there is an advantage of their approach by comparing with previous approaches.

8) The authors should also compare their results with previous publications. One of them, which is cited in the manuscript, is Weghorn and Sunyaev. In fact, this work seems to be misquoted. The authors claim that Weghorn and Sunyaev "identified 147 genes with strong negative selection", but that study in fact found very few genes under significant negative selection (<10 applying a q-value cutoff of 0.1) and Weghorn and Sunyaev concluded that "the signal of negative selection is very subtle". Zapata et al., 2018 identified stronger signals of negative selection. The identified genes and functions were partly the same as in the here presented work (eg GLUT1). The authors should compare their results to these and other previous results.

9) Furthermore, there is recent evidence that correcting for mutational signatures and nucleotide-context composition has a large impact when quantifying selection (see e.g. Zapata et al., 2018, van den Eynden et al., 2017, Martincorena et al., 2017), and this is a relevant aspect in the current lines of discussion in the context of negative selection in tumor evolution (see for example Van den Eynden et al., Nature Genetics. 2019). The authors should show that their main observations hold when the mutational signatures and/or trinucleotide context is taken into account.

10) Related to this, the authors described a clustering-based method to detect genes that deviate from an average proportion of mutations (nonsynonymous, nonsense and synonymous) to infer selection. However, by only using the observed mutations (nonsyn, syn, nonsense), the underlying base-pair composition is ignored. Genes that have a high likelihood of acquiring nonsense mutations will show a deviation from the rest of the genes due to their composition and not due to selection. The authors should recalculate their metrics by performing this correction before reaching the conclusion on the number and identity of the genes.

Use of controls

11) The reviewers also indicated the lack of sufficient controls. To improve the robustness of their method, it was suggested to assess the results after varying several of the conditions. For instance, to circumvent the limitation of the lack of mutations to detect negative selection, the authors study only transcripts with more than 100 mutations. The authors should compare their results using different cut-offs for the minimum number of mutations (50,100,500), and check the performance of their method and whether their results are robust.

12) Other variations that the authors should consider is to stratify data based on tumor type and mutation burden, since mixing samples with different evolutionary histories might confound the signal of negative selection. As an additional control, a reviewer suggested to perform the same analyses using the germline mutations to separate the genes into cancer specific or cell essential.

13) An additional control to be performed by the authors was related to the origin of the mutations. The file CosmicMutantExport.tsv contains both mutation data from targeted and genome- / exome-wide screens. Targeted data should be excluded (if the authors didn't do so already). Otherwise their analysis will be highly biased towards well characterized cancer genes.

Statistical tests

14) The reviewers also agreed that there is a general lack of statistical tests in the results. For instance, "the mean parameters of TSGs differ markedly from those of passenger genes in that rNS and rNM values are higher", but these comparisons should be done with appropriate statistical tests to assess the significance. Similar tests should be performed throughout the manuscript.

15) A very interesting idea in the paper highlighted by the reviewers is that by combining their proposed metrics they can differentiate between oncogenes and tumor suppressors. It would be convenient to have a visual interpretation on how different genes can be only oncogenic, only tumor suppressors, or both, depending on which sites are hit. It is important to note though that similar classifiers have been developed (Schroeder et al., 2014), so it would strengthen the claims of the study to provide a comparison with those methods.
