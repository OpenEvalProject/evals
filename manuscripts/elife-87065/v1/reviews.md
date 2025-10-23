# Peer review - Round 1

Editors:
- Nicole C Dubois, Icahn School of Medicine at Mount Sinai United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87065.3.sa0](https://doi.org/10.7554/eLife.87065.3.sa0)

This manuscript describes a useful tool for quantitative assessment of sarcomere structures in healthy and perturbed cardiomyocytes grown in vitro. The work is solid, and the methods, data and analyses broadly support the claims with only minor weaknesses. The tool will be relevant to biologists working on and interested in obtaining quantitative information on sarcomere structure, function and development.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87065.3.sa1](https://doi.org/10.7554/eLife.87065.3.sa1)

This manuscript by Neininger-Castro and colleagues presents a novel automatic image analysis method for assessing sarcomeres, the basic units of myofibrils and validates this tool in a couple of experimental approaches that interfere with sarcomere assembly in iPSC-cardiomyocytes (iPSC-CM).

Automatic quantification of sarcomeres is definitely something that is useful to the field. I am surprised that there is no reference in the manuscript to SarcTrack, published by Toepfer and colleagues in 2019 (PMID 30700234), which has exactly the same purpose. The advantage of the image analysis software presented in the current manuscript appears to me to be that it can cover both mature sarcomeres and nascent sarcomeres in premyofibrils effectively.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87065.3.sa2](https://doi.org/10.7554/eLife.87065.3.sa2)

Neininger-Castro et al report on their original study entitled "Independent regulation of Z-lines and M-lines during sarcomere assembly in cardiac myocytes revealed by the automatic image analysis software sarcApp", In this study, the research team developed two software, yoU-Net and sarcApp, that provide new binarization and sarcomere quantification methods. The authors further utilized human induced pluripotent stem cell-derived cardiomyocytes (hiCMs) as their model to verify their software by staining multiple sarcomeric components with and without the treatment of Blebbistatin, a known myosin II activity inhibitor. With the treatment of different Blebbistatin concentrations, the morphology of sarcomeric proteins was disturbed. These disrupted sarcomeric structures were further quantified using sarcApp and the quantification data supported the phenotype. The authors further investigated the roles of muscle myosins in sarcomere assembly by knocking down MYH6, MYH7, or MYOM in hiCMs. The knockdown of these genes did not affect Z-line assembly yet the knockdown of MYOM affected M-line assembly. The authors demonstrated that different muscle myosins participate in sarcomere assembly in different manners.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87065.3.sa3](https://doi.org/10.7554/eLife.87065.3.sa3)

Neininger-Castro and colleagues developed software tools for the quantification of sarcomeres and sarcomere-precursor features in immunostained human induced pluripotent stem cell-derived cardiac myocytes (hiCMs). In the first part they used a deep-learning- based model called a U-Net to construct and train a network for binarization of immunostained cardiomyocyte images. They also wrote graphical user interface (GUI) software that will assist other labs to use this approach and made it publicly available. They did not compare their approach to existing ones, but example from one image suggests their binarization tool outperforms Otsu thresholding binarization.

In the second part they developed a software tool called sarcApp that classifies sarcomere structures in the binarized image as a Z-Line or Z-Body and assigns each to either a myofibril or to stress fibers. The tools can then automatically count and measure multiple features (33 per cell and 24 per myofibril) and report them on a per-cell, per-myofibril, and per- stress fiber basis.

To test the tools they used Blebbistatin to inhibit sarcomere assembly and showed that the sarcApp tool could capture changes in multiple features such as fewer myofibrils, fewer Z-Lines, decreased myofibril persistence, decreased Z-Line length and altered myofibril orientation in the Blebbistatin treated cells. With some changes the tool was also shown to quantify sarcomeres in titin and myomesin stained cardiomyocytes.

Finally they used sarcApp to quantify the changes in sarcomere assembly after siRNA mediated knockout of MYH7, MYH7, or MYOM. The analysis indicates that neither MYH6 nor MYH7 knockdown perturbed the assembly of Z- or M-lines, and that knockdown of MYOM perturbed the A-band/M-Line but not the Z-Line assembly according to features captured by the sarcApp tool.

Overall the authors developed and made publicly available an excellent software tool that will be very useful for labs that are interested in studying sarcomere assembly. Multiple features that are difficult to measure or count manually can be automatically measured by the software quickly and accurately.

There are however some remaining questions about these tools:

1. The binarization tool which is tailored to sarcomere image binarization appears promising but was not systematically compared with existing approaches. Example from one cell suggests it outperforms Otsu's binarization approach.

2. How robust is the tool? The tool was tested on images from one type of cardiomyocytes (hiCMs) taken from one lab using Nikon Spinning Disk confocal microscope equipped with Apo TIRF Oil 100X 1.49 NA objective or instant Structured Illumination Microscopy (iSIM), using deconvolution (Microvolution software) and in a specific magnification. It remains to be seen whether the tool would be equally effective with images taken with other microscopy systems, with other cardiomyocytes (chick or neonatal rat), with different magnifications, live imaging, etc. The authors state that this approach is also useful in other situations, but the data is not included in this manuscript.

3. The tool was developed for evaluation of sarcomere assembly. The authors show that for this application it can detect the perturbation by Blebbistatin, or knockdown of sarcomeric genes. It remains to be seen if this tool is also useful for assessment of sarcomere structure for other questions beside sarcomere assembly and in other sarcomere pathologies.
