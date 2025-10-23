# Peer review - Round 1

Editors:
- Kristin Tessmar-Raible, https://ror.org/03prydq77 University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78300.sa0](https://doi.org/10.7554/eLife.78300.sa0)

This methodological manuscript is of interest to the fields of neural development, tissue morphogenesis, and image analysis technologies. The authors developed an image registration tool and created a digital atlas to reflect the anatomical distribution of neuronal birthdates in the developing zebrafish hindbrain. The provided resources can be very useful to monitor temporal changes in tissue growth.


---

# Peer review - Round 1

Editors:
- Kristin Tessmar-Raible, https://ror.org/03prydq77 University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78300.sa1](https://doi.org/10.7554/eLife.78300.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "The Digital 3D-Atlas MAKER (DAMAKER): a dynamic and expandable digital 3D-tool for monitoring the temporal changes in tissue growth during hindbrain morphogenesis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Richard White as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Venera Weinhardt (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers agreed that the paper needs to improve significantly on the following three points:

1 – To improve the temporal content of the method by additional experiments on time-lapse imaging and corresponding controls.

2 – To show inter-individual variability, which should be possible without additional experiments by incorporation of (most probably) existing data.

The details on points 1 and 2 are outlined in the constructive recommendations to the authors and public reviews. Please also note that the reviewers consented that while analyses of mutants would be nice to add, they are not required for the publication of this article.

3 – To deposit software along with explanations/manuals on how to use and extend it further. The two links that are currently provided send to the identical webpage on which neither Macros nor R code can be found.

Reviewer #2 (Recommendations for the authors):

1. Much higher 3D magnifications are needed in order to evaluate the morphogenetic changes of particular cell types and domains in a greater resolution.

2. More experimental data is required in order to further convince how the new imaging protocols provide many more detailed answers compared to traditional imaging tools.

3. Validation of the technology's strength should be provided by asking a physiological question about the developing hindbrain. Many relevant mutant lines are available (including in the author's lab) that can serve to demonstrate how the DAMAKER protocol is indeed an innovative and original strategy to study brain development in a manner that was absent in previous studies.

4. As opposed to the numerous notions of the authors regarding the development of a novel code to provide a temporal 3D atlas, the actual data presented to demonstrate this capacity is rather limited. Hence, the text should be more balanced in that aspect.

Reviewer #3 (Recommendations for the authors):

The manuscript is readable but at places is difficult to understand due to a lack of information and broader terms. The following aspects can be improved:

– It is stated that manual segmentation of masks was performed. Masks of what exactly? The fluorescence imaging is per se is either signal (1) or not (0). Therefore, the whole purpose of masking is therefore unclear.

– Supplementary figure 1, panels E and F please make sure to clarify what is measured and what is calculated value? As I understand NDD is measured and PD is simply calculated by substruction, thus the same std and inverted look of plots.

– A supplementary figure with corresponding stages of zebrafish development would be very helpful for those outside of the zebrafish community.

– I think it is important to show individual variability of the data, which would help to understand the difficulties of the atlas making and justify the development of a pipeline. Please include data on multiple datasets with the same marker.

– Line 206 "Once the alignment of the HuC signal was accomplished,…". How the alignment was verified? Fijiyama to my memory uses an iterative approach, was the number of iterations fixed to 4? Was its success verified and how?

– Throughout the manuscript when reporting on the quantitative analysis of a tissue, in particular volume, you use "neurons are born". That is misleading. The analysis pipeline does not count the number of neurons but rather the volume occupied by a tissue. Please make sure to state it at least in the beginning.

– In all figures and videos please do not use a red-green colour combination. 20% of readers are colorblind.

– Please include the AP and LML coordinate system on the figures to ensure that readers with other backgrounds can understand it as well.

Finally, I could not find supporting software on your web page: https://www.upf.edu/web/pujadeslab/open-science. Considering the focus of your manuscript this is essential. Next time, please ensure the availability of your software during the review process.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A dynamic and expandable Digital 3D-Atlas MAKER for monitoring the temporal changes in tissue growth during hindbrain morphogenesis" for further consideration by eLife. Your revised article has been evaluated by the three original reviewers, as well as by Richard White (Senior Editor) and a Reviewing Editor.

We much appreciate the work you put into the revised version, and think that it is now almost suitable for publication in eLife. There is still one request on the assessment of the inter-individual variability that will be highly useful to implement, also in the perspective of the future usefulness of your work for others.

The authors quantified the interindividual variability more carefully in Figure 1-Supplement 1 and Figure 3 – Supplement 1, with the purpose of demonstrating that "interindividual variability is low". However, in all the grayscale representations, variability is clearly visible in that some non-white volume area have at least 2~3 layers of cells, and even the HuC volume of the fish quantified at the same experimental condition could have a variability of 20% (Fig1S1F and Fig3S1A andB). Instead of only claiming the "low variability", the authors should have a quantitative measurement of this variability in the manuscript, and provide the confidence level of the birthdate map. This will essentially help the users to make a decision on whether an area of interest should be followed up or is beyond the precision that can be measured by the atlas.
