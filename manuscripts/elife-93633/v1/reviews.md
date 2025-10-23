# Peer review - Round 1

Editors:
- Pingyong Xu, University of Chinese Academy of Sciences China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.93633.3.sa0](https://doi.org/10.7554/eLife.93633.3.sa0)

The important study established a large-scale objective and integrated multiple optical microscopy systems to demonstrate their potential for long-term imaging of the developmental process. The convincing imaging data cover a wide range of biological applications, such as organoids, mouse brains, and quail embryos, but enhancing image quality can further enhance the method's effectiveness. This work will appeal to biologists and imaging technologists focused on long-term imaging of large fields.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93633.3.sa1](https://doi.org/10.7554/eLife.93633.3.sa1)

Summary:

The authors are trying to develop a microscopy system that generates data output exceeding the previous systems based on huge objectives.

Strengths:

They have accomplished building such a system, with a field of view of 1.5x1.0 cm2 and a resolution of up to 1.2 um. They have also demonstrated their system performance on samples such as organoids, brain sections, and embryos.

Weaknesses:

To be used as a volumetric imaging technique, the authors only showcase the implementation of multi-focal confocal sectioning. On the other hand, most of the real biological samples were acquired under the wide-field illumination, and processed with so-called computational sectioning. Despite the claim that it improves the contrast, sometimes I felt that the images were oversharpened and the quantitative nature of these fluorescence images may be perturbed.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.93633.3.sa2](https://doi.org/10.7554/eLife.93633.3.sa2)

Summary:

This manuscript introduced a volumetric trans-scale imaging system with an ultra-large field-of-view (FOV) that enables simultaneous observation of millions of cellular dynamics in centimeter-wide 3D tissues and embryos. In term of technique, this paper is just a minor improvement of the authors' previous work, which is a fluorescence imaging system working at visible wavelength region (https://www.nature.com/articles/s41598-021-95930-7).

Strengths:

In this study, the authors enhanced the system's resolution and sensitivity by increasing the numerical aperture (NA) of the lens. Furthermore, they achieved volumetric imaging by integrating optical sectioning and computational sectioning. This study encompasses a broad range of biological applications, including imaging and analysis on organoids, mouse brains, and quail embryos, respectively. Overall, this method is useful and versatile.

Weaknesses:

What is the unique application that only can be done by this high-throughput system remains vague. Meanwhile, there are also several outstanding issues in this paper, such as the lack of technical advances, unclear method details and non-standardized figures.

Comments on revisions:

The revised manuscript has significantly improved in response to the initial review comments, particularly with the detailed additions regarding the objective lens and confocal imaging modes, which enhance the clarity and comprehensibility of the paper. While the structure and arguments are much clearer overall, there are still key issues that need to be addressed, specifically regarding algorithm validation, computational sectioning presentation, and volume imaging rate.

Algorithm Validation:

The validation of the algorithm's accuracy is not sufficiently robust. Reviewer 1's comment is entirely reasonable, and the authors should validate the algorithm's accuracy using well-established methods as ground truth. In the revised version, the authors attempt to demonstrate the fidelity of the algorithm by employing deep learning methods for high-accuracy cell recognition. However, this validation relies solely on comparisons between deep learning results and manual annotation results. The problem lies in the fact that both manual annotations and deep learning outcomes are derived from algorithm-processed data, which fails to prove the authenticity or validity of the data itself. To strengthen the validation, the authors should incorporate independent, gold-standard methods for comparison.

Computational Sectioning:

In the revised manuscript, the authors effectively demonstrate the ability of optical sectioning to improve axial resolution using fluorescent beads, as shown in Fig. S3, which is a strong point. However, the manuscript lacks a direct comparison for computational sectioning and does not provide a clear evaluation of axial resolution before and after applying computational sectioning. While some related information is included in Figs. 5.C and D, the details are insufficient, and intensity profiles are absent. I recommend that the authors include more direct visual demonstrations of computational sectioning, along with comparisons of axial resolution before and after applying computational sectioning. This would better showcase the method's effectiveness.

Volume Imaging Rate:

The manuscript currently omits critical details about the method's volume imaging rate. In the description of the quail embryo imaging experiment, key parameters such as exposure time and imaging speed are missing. Additionally, the manuscript does not discuss the maximum imaging rate supported by the system in confocal mode. The volume imaging rate is an essential factor for biological researchers to evaluate the applicability of the technique. Therefore, this information should be included, ideally in the abstract and introduction. Furthermore, the authors could describe how the volume imaging rate performs under different conditions and discuss its potential applications across various biological research contexts. Including such details would significantly enhance the paper's utility and appeal to the broader research community.

These adjustments will further strengthen the manuscript and address the reviewers' concerns effectively.
