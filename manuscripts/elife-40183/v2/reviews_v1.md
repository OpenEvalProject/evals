# Peer review - Round 1

Editors:
- Antoine M van Oijen, University of Wollongong Australia

Reviewers:
- Peter Dedecker, University of Leuven Belgium

## Review text

DOI: [10.7554/eLife.40183.020](https://doi.org/10.7554/eLife.40183.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Structured illumination microscopy combined with machine learning for the high throughput analysis of virus structure" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Arup Chakraborty as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Peter Dedecker (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

Summary:

The authors describe the use of TIRF-SIM to visualize structural heterogeneity within populations of viral particles and use machine-learning approaches to classify the different morphologies. With the speed of data acquisition and the automated classification, the method is an interesting approach to introduce robust and fast quality control of production of viral particles in an industrial setting (e.g. vaccine production).

Essential revisions:

1) Since this manuscript is a submission for the Tools and Resources section of the journal, there is less of a requirement for new mechanistic insight, but an essential need for a clear justification of why the methodology will be better than what is currently used. The reviewers commented on a lack of clear justification of the work and the need to place it in context of methods that are currently used to characterise morphologies in heterogeneous populations of viral particles. Importantly, the work should provide a quantitative analysis of how the described workflow performs compared to established workflows (the authors mention electron microscopy).

2) Also, the manuscript lacks detail in many places to truly understand what the authors did and in what order.

Not until the Materials and methods does it become clear what was being imaged in the paper, and even then, a description of the primary antibodies is not very informative with respect to what structures are being identified (envelope, capsid…?). A brief mention of what is being measured early would greatly improve the readability of the paper.

More details regarding the high throughput nature of the measurements are needed. How do the authors achieve the 500 particles/second? Do they have 1000 particles in a field of view? (1000 particles/1.8 s data collection time). How long does it take to switch between fields of view? How long does the software need to extract the 500 super resolution particles? The authors should also mention how long the analysis takes (both for training and analyzing the data with the trained algorithm).

3) The described method for feature selection hinges on the evaluation of their predictive power, though no clear definition is provided of how this is calculated.

The main issue is with Figure 4C, showing the radii of large and small spherical particles. First of all, LS and SS both seem to have the same average radius. Why? The authors also remark that "It may first appear surprising that the distribution of radius of small spherical lies within that of the large spherical but in the ELM analysis the broadening of the image structure due to the finite optical resolution is effectively removed by taking into account the point spread function (PSF)." We don't understand this argument. Consider also that the example SS and LS images (e.g. Figure 4A) are clearly different in size. Are these images then not representative?

In the next sentence, the authors argue that the SS distribution is centered on the optical resolution of the instrument, suggesting that the SS particles are effectively point-like. First of all, the LS distribution is also centered on this value, so the conclusion is that these are also point-like? Second of all, the ELM analysis is supposed to correct for this, judging by the immediately preceding sentence? It is unclear what the authors are trying to argue here.

4) When analyzing the viruses in the pool harvested fluid, the authors should quantify the percentage of unknown objects compared to measurements with purified samples. The authors could also use their method to see what impact purification has on the distribution of structures in the sample.

5) Figure 4. Extraction of the size distribution is an interesting aspect of this work. However, it is problematic that the radius of the larger spheres is often smaller than the small spheres. Particularly for spherical particles, it is possible to determine radii with better resolution than the resolution limit when using deconvolution especially for the virus, which is on the size scale of the PSF. If it is really a point-like structure, this suggest that you are not measuring viruses. Could it be unspecific binding of the secondary antibodies to the surface or individual proteins that are not associated to the viruses in this class?
