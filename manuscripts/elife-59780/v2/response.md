# Author response - Round 1

Authors:
- Dennis Segebarth ([ORCID: 0000-0002-3806-9324](https://orcid.org/0000-0002-3806-9324))
- Matthias Griebel ([ORCID: 0000-0003-1959-0242](https://orcid.org/0000-0003-1959-0242))
- Nikolai Stein
- Cora R von Collenberg
- Corinna Martin
- Dominik Fiedler
- Lucas B Comeras ([ORCID: 0000-0003-2445-3605](https://orcid.org/0000-0003-2445-3605))
- Anupam Sah ([ORCID: 0000-0001-8298-6501](https://orcid.org/0000-0001-8298-6501))
- Victoria Schoeffler
- Teresa Lüffe
- Alexander Dürr
- Rohini Gupta
- Manju Sasi
- Christina Lillesaar ([ORCID: 0000-0002-5166-2851](https://orcid.org/0000-0002-5166-2851))
- Maren D Lange
- Ramon O Tasan
- Nicolas Singewald ([ORCID: 0000-0002-0166-3370](https://orcid.org/0000-0002-0166-3370))
- Hans-Christian Pape ([ORCID: 0000-0001-6874-8224](https://orcid.org/0000-0001-6874-8224))
- Christoph M Flath ([ORCID: 0000-0002-1761-9833](https://orcid.org/0000-0002-1761-9833))
- Robert Blum ([ORCID: 0000-0002-5270-3854](https://orcid.org/0000-0002-5270-3854))

## Response text

DOI: [10.7554/eLife.59780.sa2](https://doi.org/10.7554/eLife.59780.sa2)

[Editors’ note: the authors resubmitted a revised version of the paper for consideration. What follows is the authors’ response to the first round of review.]

The reviewers and I appreciate the strengths of DeepFLaSH, and the challenges of the important problem you are attacking. We all feel that research employing fluorescence imaging will be dramatically enhanced as optimized machine learning techniques are refined that are tolerant of the particular challenges you outline. However, the current manuscript falls short of documenting the advance represented by DeepFLaSH.

We feel that any study reporting an advance must fully embrace two key demonstrations:

1) A complete and balanced comparison of the speed, ease-of-use and accuracy of the new approach (in this case, DeepFLaSH) with a full spectrum of the other tools currently available. The reviewers believe that the comparisons performed in this manuscript are not sufficient in depth or breadth. Comparisons to techniques that would not be employed by a knowledgeable user because they are known to fail (eg. a simple thresholding) only serves to weaken the confidence of the reader in the nature of the advance.

2) A use of the new approach (in this case, DeepFLaSH) to analyze a biological system and extract a publishable advance.

A manuscript expanded in this fashion, to perform a relevant bank of tests and to present a novel biological insight, would be high-impact, and would justify publication in eLife or other first-tier journals.

The thorough reviews have made it very clear to us that we did a subpar job of conveying the main intention behind the manuscript.

Our primary goal was not to establish a new method in the sense of a Deep Learning (DL) algorithm, but rather to demonstrate that a light-weight, end-to-end integration of DL methods can reliably and reproducibly verify the presence of biological effects in laboratory data – both on the inter-individual level (heterogeneous coding in lab) as well as on the inter-lab level (a network trained in lab A can with minimal re-training be used to analyze data from lab B).

Our work ultimately addresses a central concern put forward by Falk et al. (2019, Nature Methods: U-Net: deep learning for cell counting, detection, and morphometry): “U-Net learns from the provided examples. If the examples are not representative of the actual task, or if the manual annotation in these examples is low quality and inconsistent, U-Net will either fail to train or will reproduce inconsistent annotations on new data.” We suggest the following corollary of this statement: Local instantiations of deep learning models (e.g., training in a certain lab) can at most speed up the local analysis pipeline while retaining the intrinsic bias of human coders. Yet, a common integrated workflow instantiated by a light-weight tool (we called this DeepFlaSH) can additionally ensure objectivity, reliability, reproducibility and transparency through shared neural network weights.

To confirm this idea experimentally, we created typical image raw data and we used the biological model of cFOS changes after behavioral training of mice. There is no ground truth in these images showing fluorescent labels of cFOS; there is no ultimate parameter allowing signal definition. One cannot decide, whether “manual annotation in these examples is low quality and inconsistent” or not. Our experimental strategy gave us a second parameter; the behavior of the mice. Easy said: the analysis of the mouse behavior gave us a coincident parameter in order to decide whether the U-Net failed to create consistent or inconsistent data. Our main result is that the speed and flexibility of a light-weight DL workflow (such as DeepFlaSH) can be used for a higher reproducibility, reliability, objectivity and transparency in image analysis.

Over the last year, we moved forward and fully overhauled the entire study. We followed our initial idea, namely to investigate how DL can contribute to more objectivity and reproducibility of bioimage analyses. Considering these developments, we think that there is no benefit of associating this study with the prior submission.

[Editors’ note: what follows is the authors’ response to the second round of review.]

The reviewers and I would like to offer some suggested changes to the presentation, without requiring the addition of more experimental work or analyses:

1) Figures and Tables.

A) Both reviewer 2 and I found Figure 1 a bit confusing and I found at least three different ways that it could be misunderstood. The problem is that the workflow icons in the individual vertical boxes appear to lie up with the horizontal bars, which I do not believe is your intent. Please revise Figure 1 so that your intent is more clear. I suggest that changing the scale and spacing of the icons might solve it, but putting the workflow icons below the horizontal bars would make the figure only slightly larger and make you intent much more clear.

We appreciate this input. Having spent a lot of time on Figure 1 in the initial submission process we were so deep into it that we did not realize that the ordering of icons, process steps and approaches may be confusing. Looking at the figure again after 3 months, the issues you raised become directly evident. We modified the figure along your suggestions and feel that it is much easier to understand now.

B) Please use similar scales and formats for figures that readers are likely to compare, and might misunderstand. For example Figure 2—figure supplement 3 and Figure 2—figure supplement 4 are slightly different sizes, and use different scales (what the different shades of gray represent), so I found myself puzzled. Figure 5—figure supplement 3 and Figure 5—figure supplement 4 use different scales as well.

In our initial version we tried to exploit the whole greyscale space to visually distinguish the heatmap entries, using different scales for each metric (f1 score/iou). We agree that the resulting scaling differences lead to confusion when comparing across figures. We revised the figures and aligned the scales for Figure 2—figure supplement 3/ Figure 2—figure supplement 4 and Figure 5—figure supplement 3/ Figure 5—figure supplement 4.

C) Table 1, and elsewhere in the text needs attention to the number of significant figures that are displayed. Table 1 shows p-values to 5 or 4 significant figures for non-significant differences. It shows p-values to 3 significant figures for some of the significant differences. If the authors reflect on this, I believe they will agree that there is no way that the data set is sufficiently large for this number of significant figures. Furthermore, the large number of figures distract the reader from the message I believe the authors are intending to convey.

We fully agree that the limited size of these data sets also restricts the validity of the calculated p-values to less post decimal positions. We therefore reduced the number of presented post decimal positions for the calculated p-values in Table 1 to 3 and denote p-values that are smaller than 0.001 as < 0.001.

2) Language and definitions.

A) The reviewers point out that this very strong paper is not made stronger by claims that seem beyond beyond the data. These include the claim that the DL approach surpasses the experts.

B) There are terms that should be clarified or defined; in most of these cases, it might be wise to find language that is less likely to be misunderstood. These include: "invalid", "bad", "biased", "irreproducible", "appear to alter the results", "DL models are proven to…" etc. Note that all of these should be easy to resolve, but could confuse, anger and/or frustrate a reader, which will not optimize the acceptance of the important lessons of this work.

We appreciate these pointers to our usage of ambiguous terms. In the revised document we carefully rephrased the corresponding passages. We replaced the corresponding terms or replaced the sentences with more careful statements. Overstatements without solid statistical foundation such as “constantly outperform/surpass” were deleted.

Reviewer #1:

This work is high quality, employs real-world data sets from multiple sources, and addresses questions of broad interest. I recommend publication in eLife.

Reviewer #2:

In general, I really enjoyed reading this manuscript, and I think the new focus resulted in a much clearer paper compared with the previous version. As a researcher in machine learning myself, the manuscript includes several findings that I will use in my future research, especially the comparison between the various training approaches. As such, I think that the paper will be a valuable contribution to the field, and I recommend publication after my comments below (and those of other reviewers) have been addressed. Note that my expertise is in developing machine learning algorithms, and I don't have enough background in the specific biology application to feel comfortable with commenting on the validity of the biology.

1) My main concern with respect to the method is the exclusion of what the authors call “invalid” methods in the ensemble approaches. By construction, this exclusion biases the results towards better metrics. Therefore, it is not entirely clear whether the better performance of the ensemble approaches is caused by the ensemble itself, or rather simply by the fact that multiple networks were trained and “bad” networks were thrown away. This question can be answered in several ways: for example, it would already be informative to know how many networks were rejected in this way (if it is a small number compared with the total number of networks, it is not likely the improvement is due to the rejection). Even better would be to also apply the same rejection strategy to the expert model approach and see whether that improves these by the same amount (even though you would have access to the estimated GT in pure expert model applications).

Thank you for this valuable feedback! We agree that our initial manuscript did not sufficiently justify the model selection process and the impacts on model performance. Following your suggestion, we have indicated the number of discarded models in the corresponding figure legends (Figures 5, Figure 5—figure supplement 1, Figure 5—figure supplement 2) and included the model selection results in the corresponding figure source data. Moreover, we have revised the description of the model selection process (as stated in our response to the Editor).

2) My second main concern is with regards to practical application of the consensus ensemble approach. In many applications, it is very time consuming to acquire manually annotated images due to the required expertise for manual annotation and the time it takes to annotate. Therefore, getting enough manual annotations to obtain accurate consensus models might be prohibitively difficult in practice. A solution for this might be to use multiple experts, but have each expert annotate a different set of images. This would drastically reduce the required manual annotation time compared with obtaining a full consensus model, but you would still have information from multiple experts, which might improve results. For the current manuscript, it would be very informative to include this approach in the results. One way of doing this is to use the data that the authors already have, assign each of the 36 training images to one of the 5 experts, and then during training only use the manual annotation of the assigned expert for that image.

Indeed, the acquisition of annotated training data was one of the greatest challenges for our study, and it will most likely continue to be the bottleneck for future DL based studies. For this study, we avoided splitting the training images because our aim was to control the DL strategies exactly on the same images to get information about the variability between experts and expert models. During our experiments, we have already tried different approaches for model training, e.g., we trained models using all expert segmentation instead of the estimated ground truth. This approach led to an unstable training behavior (heavy oscillations of the loss function from iteration to iteration). We would argue that your suggested approach could lead to the same training instability (of course, depending on the data and the differences between expert annotations). However, we agree that there is still potential to reduce the annotation effort that should be evaluated in future studies.

3) To me Figure 1 is quite hard to read. I do get what the authors mean, but the fact that the icons in the “vertical blocks” (e.g. “data annotation” and “automated annotation”) align with the rows makes it seem that each icon in the block actually belongs to a certain row. A solution would be to rearrange the icons inside each block somewhat (e.g. by making them smaller) so that they don't line up anymore with the rows.

We modified the figure and feel that it is much easier to understand now.

4) It would be interesting to investigate what the accuracy is of an approach in which only the GT of a single expert is used, but multiple network are trained in an ensemble. In other words, a combination between the expert models and consensus ensembles, but without using the estimated GT. This would indicate whether the improvement of the consensus ensembles is not purely due to the ensemble itself. I don't expect that this will actually achieve very accurate results, so probably a short paragraph or an added sentence or two will be enough to describe these additional results in the paper.

As stated above, we trained models using all expert segmentation instead of the estimated ground truth in our initial experiments. This has led to an unstable training behavior. We think this was caused by the considerable differences in expert annotations. This approach, however, might work with less ambiguous data.
