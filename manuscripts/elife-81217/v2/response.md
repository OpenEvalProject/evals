# Author response - Round 1

Authors:
- Ziqi Yu ([ORCID: 0000-0001-8201-5481](https://orcid.org/0000-0001-8201-5481))
- Xiaoyang Han ([ORCID: 0000-0002-3007-6079](https://orcid.org/0000-0002-3007-6079))
- Wenjing Xu
- Jie Zhang
- Carsten Marr ([ORCID: 0000-0003-2154-4552](https://orcid.org/0000-0003-2154-4552))
- Dinggang Shen
- Tingying Peng
- Xiao-Yong Zhang ([ORCID: 0000-0001-8965-1077](https://orcid.org/0000-0001-8965-1077))
- Jianfeng Feng ([ORCID: 0000-0001-5987-2258](https://orcid.org/0000-0001-5987-2258))

## Response text

DOI: [10.7554/eLife.81217.sa2](https://doi.org/10.7554/eLife.81217.sa2)

Essential revisions:

The one major point raised by reviewer 2 appears to me to be the most important to properly address, as it appears the method did not work well on the reviewer's own data, casting doubt on the generalisability of the approach- the main selling point of the paper.

We thank the Editors very much. These comments are very encouraging, valuable, and constructive. We have carefully revised our manuscript based on the comments of the reviewers. Please refer to our response to the reviewers for details.

Reviewer #2 (Recommendations for the authors):

The major point I'd like to see the authors discuss is when BEN needs to be retrained on different input data and discuss techniques to improve generalizability. In the examples given and weights provided they suggest that, for example, 7T and 9.4T T2w mouse data needs different networks. This is somewhat surprising to me and suggests that the networks might be overfitting to their input data. My own tests (as described in the public review) also suggest that even subtle changes to out-of-sample data quickly degrade performance.

We thank the reviewer for the helpful comment and raise important aspects we have addressed in our paper and Github codes. The adjustments are listed as follows:

1. We have discussed briefly when BEN needs to be retrained in the second paragraph in “Discussion – Compatibility with other toolboxes and deployment”. In the revised version, we have updated the descriptions to make it clear, and also provide several video tutorials (using public ex vivo data to demonstrate). Since the initial version of BEN is intended to reproduce our results in paper, some corner cases and complex cases were not well taken into consideration. These concerns have now been well addressed in updated codes (https://github.com/yu02019/BEN).

2. The techniques for increasing generalizability have also been added to “Discussion” and BEN pipeline, e.g., orientation detection, post-processing, etc.

3. As for experiments across 7T and 9.4T T2w, BEN could adapt to these out-of-domain images without labels (zero-shot learning) , as the domain shift between 7T and 9.4T is relatively small. The quantitative results for these cross-MR scanners with various magnetic field strengths are presented in Figure 3—figure supplement 2. Without additional labels (zero-shot), BEN presents satisfactory performance on two of the three tasks, while the other two baseline methods all fail on all three tasks. In fact, we deem this to be essentially a cross-center task that disables the performances of many deep learning-based methods; BEN addresses and alleviates this problem using the "domain adaptation module" and packages it well for the general user without coding skills. Alternatively, one can train a “super-network” with big training data across different species, modalities and magnetic strengths so the network can be used in an ‘out-of-the-box' fashion. But this is difficult in practice as the animal MR experiments are very diverse in nature and there is always some “out-of-sample” testing data.

4. Besides, the original intent for cross-field strength experiments was to demonstrate BEN could provide a fast and label-efficient domain adaptation training method as a scalable tool. We can certainly provide joint-training weights that could easily meet the reviewer’s requirement. However, when deploying BEN or other toolboxes into customized data/cohorts, it is inevitable to address domain adaptation issues, suggesting the importance of our model design.

5. How to deal with out-of-sample data is a challenge for many deep learning methods. To the best of our knowledge, it is very difficult for almost all existing methods to handle the images with low quality (artifacts, field inhomogeneity, high noise, or low SNR). To solve this issue, in our model, we suggest adding several exemplary MR scans to retrain BEN; on the other hand, it could be addressed partly by post-processing or the “Monte Carlo quality assessment module” in the BEN pipeline. We will give some examples in our tutorials.

Secondly, I find that the narrative in places overstates the importance of their work, primarily since in my opinion the community has created multiple brain masking algorithms in different species that work well. Three examples include:

1) Line 17: the claim that brain extraction in animals is not fully automated; the relatively simpler brains, especially in rodents, means that image registration-based approaches to segmenting brains is quite successful and has been implemented in multiple toolkits. Similarly, the claim that the performance of registration-based methods is limited is at odds with the data.

We thank the reviewer for raising this issue. We think the success of automatic registration-based approaches depends on the quality and the number of atlases (e.g. multi-atlas registration is usually better than single-atlas one), and registration is not an easy task as the heterogeneous contrasts existing in different image spaces (e.g., native space and atlas space) might not provide enough guidance for intensity-based registration metrics. Due to the scarcity of publicly available MRI data and multi-atlases, it is generally more difficult in animal MR studies than human ones where multi-atlas registration is well established.

Alternatively, some semi-automatic registration-based approaches using one dataset-specific template atlas which have to be manually labeled (then it has similar or identical experimental conditions, MR parameters, and image properties) present better and more stable performance on the current experimental cohort than fully automated methods using public atlas from different cohorts or imaging centers. There still remain limitations to semi-automatic registration-based methods: (1) If registration-based methods fail, it’s hard to adjust, thus requiring laborious manual corrections. (2) The dataset-specific template mask is usually manually annotated, which is another time-consuming step in addition to the registration. (3) Based on our results (Author response table 1), registration-based methods performed unsatisfactory on fMRI data and scans with thick slice thickness.

SkullStrip: semi-automatic registration-based method. (ASD: average surface distance. HD95: 95% Hausdorff distance).

We have conducted comparisons using such semi-automatic registration-based approaches, “SkullStrip” [1] (based on NiftyReg). The results are presented in Author response table 1 as follows. As a conclusion, though [1] could perform well in some cases, it seems that its performance suffers from functional MR data and scans with thick slice thickness (e.g., Mouse-ASL-11.7T and Mouse-T2WI-9.4T images, etc.). Besides, BEN’s results show a much lower HD95 value, which means higher boundary agreement with the ground truth. One more point we want to emphasize is that the computational speed for such registration-based methods (which take hours for one small cohort) is much slower than BEN (which only takes several minutes).

Moreover, unlike registration-based methods (it’s hard to adjust when dealing with failed segmentations), BEN could improve its output by updating annotations of failed cases, which is like a “human-in-the-loop” manner. In addition, BEN‘s clear running logs and interactive training procedures would further provide more information for researchers.

[1] Delora A, Gonzales A, Medina C S, et al. A simple rapid process for semi-automated brain extraction from magnetic resonance images of the whole mouse head[J]. Journal of neuroscience methods, 2016, 257: 185-193.

2) It is not clear to me why the authors would expect FSL or FreeSurfer to work on rodents out of the box, given that the algorithms were never tuned for non-human brains (as far as I am aware). Their inclusion for animal brain segmentation tasks thus appears to be a bit of a straw man.

We thank the reviewer for this comment. We know that FSL/FreeSurfer are designed for human beings, and are not designed for rodents. Here we include these tools just for parallel comparison (otherwise we do not have enough comparison), not criticizing these well-established tools. Since such publicly available animal neuroimaging tools are scarce, we include these tools in our consideration of the influence and seminal role of these tools, and it’s impractical to find a more suitable substitute for each species and modality. Indeed, we focus on the comparison of BEN and FSL/FreeSurfer in human brain performance (Figure 4 E, J and O and Figure 5—figure supplement 3). As BEN could achieve competitive performance on human brains compared with FSL/FreeSurfer and the transferability of BEN made it not bound to specific species or modality, readers can easily deploy BEN on their customized dataset, without the requirement of complex programming skills or mathematics knowledge.

3) I also found Figure 7 and the related arguments about why BEN is necessary a bit odd; any decent registration/segmentation pipeline would incorporate brain masking, so the comparison of with and without masking is also a false contrast. There are lots of interesting ideas in this manuscript that it does not need these types of strawman arguments, so I would suggest removing this section entirely or alternately comparing the inclusion of BEN for masking as compared to alternate pipelines with masking included as well.

We thank the reviewer for raising this valuable point. We have moved Figure 7 into supporting materials (Figure 5—figure supplement 1) and revised it (BEN vs AFNI-rats) in the revised version. The reason why we did not remove this figure is that we think this figure is an important example application to show the impact of BEN on downstream analysis. We agree that for human studies, brain masking is already integrated in the standard MR brain image processing pipeline, e.g. FSL or Freesurfer. Yet in animal studies, there are no standardized pipelines for decent animal brain segmentation/registration. Therefore, it is essential to show the strength of BEN in improving downstream analysis and its potential to be incorporated into a recommended animal MR brain processing pipeline.
