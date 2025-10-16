# Peer review - Round 1

Editors:
- Karsten Kruse, University of Geneva Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94391.3.sa0](https://doi.org/10.7554/eLife.94391.3.sa0)

In this important work, a quantitative analysis method for three-dimensional morphogenetic processes during embryonic development is introduced. The proposed method is a pipeline combining several methods, allowing quantitative analysis of developmental processes without cell segmentation and tracking. Upon application of their method, the authors obtain convincing evidence that ascidian gastrulation is a two-step process. This work should be of interest to a broad range of developmental biologists who aim to obtain a quantitative understanding of morphogenesis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94391.3.sa1](https://doi.org/10.7554/eLife.94391.3.sa1)

Summary:

The authors propose a new method to quantitatively assess morphogenetic processes during organismal development. They apply their method to ascidian morphogenesis and thus find that gastrulation is a two-step process.

The method applies to morphogenetic changes of surfaces. It consists of the following steps: first, surface deformations are quantified based on microscopy images without requiring cellular segmentation and tracking. This is achieved by mapping, at each time point, a polygonal mesh initially defined on a sphere to the surface of the embryo. The mapped vertices of this polygonal mesh then serve as (Lagrangian) markers for the embryonic surface. From these, one can infer the deformation of the surface, which can be expressed in terms of the strain tensor at each point of the surface. Changes in the strain tensor give the strain rate, which captures the morphogenetic processes. Second, at each time point, the strain rate field is decomposed in terms of spherical harmonics. Finally, the evolution of the weights of the various spherical harmonics in the decomposition is analysed via a wavelet analysis. The authors apply their workflow to ascidian development between 4 and 8.7 hpf. From their analysis they find clear indications for gastrulation and neurulation and identify two sub-phases of gastrulation, namely, endoderm invagination and 'blastophore closure'.

Strengths:

The combination of various tools allows the authors to obtain a quantitative description of the developing embryo without the necessity of identifying fiducial markers. Visual inspection shows that their method works well. Furthermore, this quantification then allows for an unbiased identification of different morphogenetic phases.

Weaknesses:

At times, the explanation of the method is hard to follow, unless the reader is already familiar with concepts like level-set methods or wavelet transforms. Furthermore, the software for performing the determination of Lagrangian markers or the subsequent spectral analysis does not seem to be available to the readers.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94391.3.sa2](https://doi.org/10.7554/eLife.94391.3.sa2)

Summary:

In this manuscript, the authors proposed a method to quantitatively analyze 3D live imaging data of early developing embryos, using the ascidian development as an example. For this purpose, the previously proposed level set method was used to computationally track the temporal evolution of reference points introduced on the embryo surface. Then, from the obtained three-dimensional trajectories, the velocity field was obtained, from which the strain rate field was computed. The strain rate field was analyzed using spherical harmonics.

In this paper, the authors focused on the modes with lower order with real coefficients. The time evolution of these modes was analyzed using wavelet transforms. The results obtained by the pipeline reflected the developmental stages of ascidian embryos.

Strengths:

In this way, this manuscript proposes a pipeline of analyses combining various methods. The strength of this method lies in its ability to quantitatively analyze the deformation of the entire embryo without the requirement for cellular segmentation and tracking.

Weaknesses:

The mathematics behind this method is not straightforward to understand. The value of this method will be understood as analyses of real data using this method accumulate.

Comments on revised version:

I have reviewed the revised manuscript and the reply from the authors. All concerns have been addressed appropriately.
