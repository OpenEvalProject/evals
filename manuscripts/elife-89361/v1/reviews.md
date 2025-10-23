# Peer review - Round 1

Editors:
- Eunji Cheong, Yonsei University Republic of Korea

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89361.3.sa0](https://doi.org/10.7554/eLife.89361.3.sa0)

The manuscript introduces an important and innovative non-AI computational method for segmenting noisy grayscale images, with a particular focus on identifying immunostained potassium ion channel clusters. This method significantly enhances accuracy over basic threshold-based techniques while remaining user-friendly and accessible, even for researchers with limited computational backgrounds. The evidence supporting the method's efficacy is convincing. Its practical application and ease of use make it a tool that will benefit a wide range of laboratories.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89361.3.sa1](https://doi.org/10.7554/eLife.89361.3.sa1)

The manuscript introduces a valuable and innovative non-AI computational method for segmenting noisy grayscale images, with a particular focus on identifying immunostained potassium ion channel clusters.

Strengths:

(1) Applicability and Usability: The method is exceptionally accessible to biologists and researchers without advanced computational expertise. It offers a highly practical alternative to AI-based methods, which often require significant training data and computational resources, making it an excellent choice for a broader range of laboratories.

(2) Proof-of-Concept: The manuscript provides compelling evidence through multiple experiments, showcasing the method's superior performance over traditional threshold-based techniques, particularly in noisy environments. The dual immuno-electron microscopy experiments further reinforce the robustness and effectiveness of this approach.

(3) Clarity and Methodology: The manuscript is exceptionally well-written, with clear and concise descriptions that effectively highlight the method's advantages. The detailed figures and comprehensive references greatly enhance the manuscript's credibility and strongly support the claims made.

Weaknesses:

The manuscript does not include comparisons with more advanced segmentation techniques, particularly those based on artificial intelligence. While the authors have provided a rationale for this decision, including such comparisons could have enriched the discussion and offered additional insights. Additionally, there are some concerns about the computational demands of the method, especially when applied to large-scale or 3D image analysis. Although the authors have shared some computational data, further optimization or practical recommendations would enhance the method's utility. Initially, the manuscript lacked a data and code availability statement, which could have limited the method's accessibility. However, this issue has since been resolved, with the code now being made available to the community. Lastly, while the findings related to Kv4.2 in the thalamus are noteworthy, they might achieve even greater impact if presented in a separate paper. Nevertheless, the authors have chosen to retain these results within the current manuscript to strengthen the overall narrative and relevance.

We appreciate that the authors have provided thorough explanations for their original choices. These justifications offer a clearer understanding of their approach and the reasons behind the presentation of the data.

Conclusion:

The revised manuscript successfully addresses the majority of the reviewers' concerns, presenting a strong case for the proposed segmentation method. The method's ease of use for non-experts in AI, combined with its proven effectiveness in proof-of-concept experiments, positions it as a valuable addition to the field. While the manuscript could benefit from incorporating comparisons with more advanced segmentation methods and offering a more detailed discussion of computational requirements, it remains a robust contribution. The decision to include the Kv4.2 findings within the paper is well-justified by the authors, though these results could potentially have an even greater impact if published separately.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89361.3.sa2](https://doi.org/10.7554/eLife.89361.3.sa2)

Summary:

The manuscript by David et al. describes a novel image segmentation method, implementing Local Moran's method, which determines whether the value of a datapoint or a pixel is randomly distributed among all values, in differentiating pixel clusters from the background noise. The study includes several proof-of-concept analyses to validate the power of the new approach, revealing that implementation of Local Moran's method in image segmentation is superior to threshold-based segmentation methods commonly used in analyzing confocal images in neuroanatomical studies.

Strengths:

Several proof-of-concept experiments are performed to confirm the sensitivity and validity of the proposed method. Using composed images with varying levels of background noise and analyzing them in parallel with the Local Moran's or a Threshold-Based Method (TBM), the study is able to compare these approaches directly and reveal their relative power in isolating clustered pixels.

Similarly, dual immuno-electron microscopy was used to test the biological relevance of a colocalization that was revealed by Local Moran's segmentation approach on dual-fluorescent labeled tissue using immuno-markers of the axon terminal and a membrane-protein (Figure 5). The EM revealed that the two markers were present in terminals and their post-synaptic partners, respectively. This is a strong approach to verify the validity of the new approach for determining object-based colocalization in fluorescent microscopy.

The methods section is clear in explaining the rationale and the steps of the new method (however, see the weaknesses section). Figures are appropriate and effective in illustrating the methods and the results of the study. The writing is clear; the references are appropriate and useful.

Weaknesses:

While the steps of the mathematical calculations to implement Local Moran's principles for analyzing high-resolution images are clearly written, the manuscript currently does not provide a computation tool that could facilitate easy implementation of the method by other researchers. Without a user-friendly tool, such as an ImageJ plugin or a code, the use of the method developed by David et al by other investigators may remain limited.

This weakness is eliminated in the revision, which now provides the approach as a Matlab tool.
