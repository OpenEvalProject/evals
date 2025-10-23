# Peer review - Round 1

Editors:
- Hamid Mohammadi, Francis Crick Institute United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.40162.047](https://doi.org/10.7554/eLife.40162.047)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Motion Sensing Superpixels (MOSES) is a systematic framework to quantify and discover cellular motion phenotypes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Roberto Cerbino (Reviewer #3).

As you will note, the three expert reviewers find some merit in the MOSES method but raise many issues that preclude publication. As we feel the additional work needed to address the issues raised by the reviewers would take more than two months to complete, we are returning your submission to you now in case you wish to submit elsewhere for speedy publication. Further, the number and complexity of these issues make the editorial team reluctant to encourage a resubmission unless a very substantial amount of additional work was performed. In this case, eLife would be willing to look at a revised paper. Please note that it would be treated as a new submission with no guarantees of acceptance. The two most critical factors from an editorial perspective are:

i) Demonstrating the utility of the method on a diverse range of imaging inputs (reviewer #3 point #5 – there is also a reference to some suggested data) and;

ii) Increased biological measurements, including analysis of proliferation and/or cell density. Given that this study is focused on a new technique, the final decision on this work will be highly dependent on convincingly demonstrating the broad utility of the methodology to the cell migration and tissue morphogenesis community. In addition, it will be important to address the technical issues raised, including out of plane movement or loss of cells, further analysis of the 'boundary', and improving the readability of the study.

Our decision has been reached after consultation between the reviewers.

Reviewer #1:

In the manuscript "Motion Sensing Superpixels (MOSES): A systematic framework to quantify and discover cellular motion phenotypes", Zhou et al. present a new method for measuring cell motility in epithelial sheets and apply this to boundary formation in Barrett's Esophagus.

The approach presented fills the technical gap between PIV/Optical flow measurements and single-cell tracking and provides a method to characterise, and through PCA, discover, motion phenotypes within 2D epithelia. This is certainly a technically interesting concept that is relatively simple to implement and provides insight into motion phenotypes within a tissue. This method will be broadly applicable to many problems in characterising cellular motion. In general I find the manuscript well written and comprehensive in its description of the technique, but not particularly easy to read.

One of the difficulties is that it is unclear to me whether the authors intend to reveal new insight into the fundamental phenomena or simply provide a framework for automating the analysis for e.g. drug discovery. I would argue that cell state (sub cellular protein levels, cell cycle, cell death/extrusion, as examined in Schmitz et al., 2010, Pau et al., 2013, Held et al., 2010) are equally important and are not addressed by the current method.

In the present manuscript, only the cell motion is considered and yet cell proliferation/density is likely to be very important also. Can the authors provide cell density measurements (a proxy for cell proliferation) as a function of time, perhaps using the CNN counting approach, to give some estimate of motion versus proliferation?

This would be particularly interesting in light of the experiments involving titration of EGF. These are very interesting and provide some insight into how collective dynamics/cell adhesion are important in the tissue mechanics in general.

Another consideration is that of axial/upward motion at the interface between the two epithelial monolayers as they meet. Presumably the MOSES approach would register very little motion in a region where cells are being extruded upward (as in Figure 1B). How do the authors envisage addressing this?

Overall, I think that this is a technically interesting manuscript, which provides a set of tools for measuring and characterising cell motion phenotypes from high-throughput time-lapse imaging. This is likely to be a broadly useful tool for the community and addresses a long-standing problem of characterising mesoscale behaviour with close to single-cell accuracy. In my opinion, a revised manuscript would need to provide some additional information regarding the proliferation/density/state of cells within the tissue also.

Reviewer #2:

In this study, the authors utilized their newly developed mesh-based computational framework, MOSES, to analyze the collective motion of the cells and interactions between epithelial monolayers before and after their lateral collision. They have examined three main epithelial interactions that occur in normal esophagus to esophageal adenocarcinoma progression. These interactions (Video 2) lead to formation of a stable boundary with highly dynamic motion of the two cell populations after collision (in squamous-squamous interactions), a stable boundary with less dynamic motion of cell populations after collision and having squamous monolayer pushed by columnar monolayer (squamous-columnar), and no boundary formation with retraction of squamous cell population after collision (squamous-cancer). Authors mainly define two measurements (boundary formation index and motion stability index) to quantify the differences of these boundaries. Both measurements result in selection of squamous-columnar as stable boundary while leave the other two cell combinations in the "unstable boundary" category. Further, authors investigate the effect of activation of EGFR signaling pathway in boundary formation using MOSES. While the approach is appropriate, the current level of analyses does not provide substantial enough improvement relative to other works to justify publication in eLife. There are a number of critiques that authors should address before considering this manuscript for publication.

1) Although the nature of boundaries between squamous-squamous and squamous-cancer are distinct, both are considered as "no boundary" based on boundary index analysis and "unstable boundary" based on stability index analysis. Authors should define new measurements to extract the differences between these two boundaries.

2) As stated by the authors, PIV can be also used for motion extraction in dense monolayers. Authors should clearly state how potential users might benefit using MOSES that otherwise would not be possible using PIV.

3) How would the mesh analysis be affected in case that there would be no continuity in monolayers after collision (i.e. occurrence of detached patches of cells after collision)? Could it be captured in disorder index analysis?

4) Authors have used no serum condition in order to disrupt the cell-cell contact within the monolayers. As serum may affect numerous cell functions, it is not clear if loss of collective sheet migration is because of the reduced cell-cell contacts. Authors are encouraged to use cells that have deleted intercellular adhesion (e.g. α catenin).

5) It would be beneficial to measure migratory behavior of each superpixel with respect to its distance from the boundary before and after collision.

6) How may the analyses change in cases that a combination of stable and unstable boundaries exist in the same field of view?

7) Authors state that in squamous-squamous interactions when cells are exposed to 20 ng/ml of EGF the values of boundary and stability indices are similar to that of squamous-cancer interactions. However, there is no retraction observed in squamous-squamous interactions (Video 7). Again, this needs to be resolved.

Reviewer #3:

The manuscript under review describes a method (MOSES) to quantify cell dynamics. The method is tested with epithelial monolayers made of different cell types. MOSES appears to be an interesting approach to the quantification of cell dynamics. However, for the reasons outlined below, I cannot recommend publication of the manuscript in the present form.

1) The paper is too technical to be really useful for potential users. In particular:

1a) The description of the track filtering and mesh formulation steps are so involved that in the end, I did not understand how a mesh is generated and used.

1b) In a similar manner, the boundary formation index (and to some extent also the motion stability index) is introduced in a way that requires a bona fide effort from the reader to believe that it really measures what is claimed. In my view, a methodological paper like this one, does not benefit from having all the important definitions in the Materials and methods section. Also, it would be greatly appreciated to be able to understand why the proposed parameters for the quantification of the cell dynamics outperform other possible choices.

1c) There are parts that are incomprehensible, such as for instance the paragraph entitled Automated cell counting with convolutional neural networks. This is a pity because the principal component analysis represents one of the most promising features of the method.

1d) Some quantities are not sufficiently defined. For instance, how is TrackMate similarity in Figure 2—figure supplement 2C defined? How is the distance defined in the vertical axis of Figure 1 - figure supplement 5B?

1e) Some choices are not clearly explained: why the cut-off for boundary formation and stability are defined by using the standard deviation? This choice seems to me to be an ambiguous one. For instance, a cut-off for boundary formation is "defined statistically as one standard deviation higher than the pooled mean of all three combinations (Figure 3C). Above this cut-off, cell combinations are categorised as forming a boundary". Surprisingly, a few lines below the authors write "Similarly, experiments in 0% serum were used to set the global motion stability threshold (0.87), one standard deviation below the pooled mean" (Figure 3D). Can the authors explain this asymmetry? The use of standard deviations for fixing thresholds would need in my view that a band exists (pooled mean +/- standard deviation) where the behavior is not determined. Only below mean + sd and above mean - sd a clear behavior could be attributed.

I suggest that the authors consider seriously revising the structure of their paper to make it understandable to a wide audience and to enable the potential reader to properly evaluate the powerfulness and the limitations of the proposed approach.

2) The literature review presented in the Introduction is also not clear, being a puzzling mix of methods to quantify the cell dynamics (such as tracking and PIV) and models (such as the vertex model). To me, the authors fail in merging successfully these two branches of literature and, in particular, in explaining where does MOSES fit and why the previously available tools, are not as good as MOSES in terms of robustness, sensitivity, automatization, and unbiasedness.

3) There are some claims that seem not to be supported by the experimental results. Typical examples are:

3a) Subsection “In-vitro model to study the spatio-temporal dynamics of boundary formation between different cell populations”, first paragraph: Figure 1—figure supplement 2 is cited in support of the fact that cells labeled with different color dye move in a similar way. Inspection of SF2(Figure 1 - figure supplement 2) shows that in some cases the MSD can differ by about one order of magnitude. How is it that the authors consider this a proof of similarity?

3b) The method is allegedly working perfectly in an automatic and unbiased fashion. How comes that the boundary in Figure 3—figure supplement 9A does not seem to be adequately determined?

3c) The statement "The mesh disorder index showed statistically significant increases with EGF concentration" does not seem to be supported by the data in Supplementary Figure 9, where a non-monotonic behavior would also be compatible with the data.

4) There are some claims whose general validity (i.e. in other experiments) is rather dubious.

4a) The Authors claim that "individual cells behave similarly to their neighbors so global motion patterns can be used as a proxy to study single cell behavior". I doubt that this is always true. For instance, for the liquid states found in [Nature Materials 16, 587-596 (2017)] I believe that this claim wouldn't be true.

4b) Given that the L1-norm at is not defined, what is the general validity of the statement "We use L1 for robustness as this value is > 1"?

5) The authors propose MOSES as a robust, sensitive, automatic and unbiased method and I trust them that this might be true. However, the current version of the manuscript proves that MOSES works fairly well in the few cases selected by the authors and it is not clear to me that it could be really used successfully in all other cases. Maybe, the authors could comment on this by suggesting cases in which they expect MOSES to work and cases where they think it would not. For instance, do the authors think that MOSES would work for the experiments in [Nature Materials 16, 1029 (2017)]?

In summary, I do see some potential in MOSES but the current version is not making a good job in explaining clearly what the method does, why is it better than other approaches and when it should be applicable. I hope that the authors will be able to address the above issues.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "Motion Sensing Superpixels (MOSES): A systematic framework to quantify and discover cellular motion phenotypes" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Roberto Cerbino (Reviewer #2); Alison McGuigan (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

This manuscript is well improved and of high scientific value; however two of the reviewers raised several significant points that need clarification. These should be addressed in detail to resolve their concerns. The issue of serum-free condition as negative control may require additional experimentation for validation.

Reviewer #1:

The second version of the manuscript has been improved extensively and reads better than the first one. However, there are a few criticisms the authors should address before considering this manuscript for publication.

An important feature of the tissue boundaries is their shape. It would be beneficial if authors could also incorporate the analysis of boundary roughness in their computational framework.

Authors stated that the "cancer cell line OE33 pushed EPC2 out of the field of view". Since the traction forces applied at the interface between the two sheets is not presented in the manuscript, it is unclear whether the EPC2 cells retracted upon contact with OE33 cells or are continuously pushed by application of physical forces exerted by OE33 cells at the interface.

Authors have conducted new experiments, where the impact of depletion of Ca2+ on boundary formation is examined, to elucidate how the absent of cell-cell contact may disrupt the collective motion of the epithelial sheets. However, it is still unclear how serum depletion impacts the proliferation rate of the cells and that affects the collective motion of the sheets.

In conclusion, authors should present how much their computational framework can potentially improve our knowledge in biological processes and how it could be used to tackle new challenges.

Reviewer #2:

The authors have done an extensive amount of work to try to address all the reviewers' comments. As a result, the manuscript is now more clear and convincing in describing the proposed MOSES approach for quantifying the motility of cells belonging to a collective. I thus recommend publication in eLife.

Reviewer #3:

This paper presents a potentially useful tool to enable quantification of cell movement from large numbers of movies to better identify molecules that modulate collective cell migration dynamics. The scale of the data collected is impressive but I found this paper incredibly challenging to read and to understand what the data measurements physically represented and what these measurements meant biologically for our understanding of cell cooperation during boundary formation. Furthermore, I did not really understand the argument made by the authors that serum free represents no boundary formation versus for example delayed boundary formation since cells will move slower and proliferate less (and have a gap to fill before a boundary can form). This manuscript is interesting but is not currently accessible to a broad readership in my opinion.

The major comment I had that I think could significantly improve the impact of the work is can the authors better highlight the functional importance of the metrics they are quantifying in terms of the biological behaviours. For example is a boundary the best thing to be describing here or is wound healing a better example to be able to extract out different cell movement regimes to highlight the power of the tool? I could not understand how the metrics highlighted here could give me new insight into how a boundary is formed therefore it was not clear what I could learn using the tool.

The use of serum free medium to prevent boundary formation does not seem the most robust approach as this also likely impacts cell movement and proliferation, which will impact the timing required to form the boundary in the model being used (since the cells have to proliferate to fill the open space between the two cell domains. I am not sure of the logic behind specifying that doing things in serum free media gives a negative control that corresponds to a no-boundary formation case.
