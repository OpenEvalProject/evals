# Peer review - Round 1

Editors:
- Raymond E Goldstein, University of Cambridge United Kingdom

Reviewers:
- Timothy E Saunders, National University of Singapore Singapore

## Review text

DOI: [10.7554/eLife.42646.052](https://doi.org/10.7554/eLife.42646.052)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "Retinal stem cells modulate proliferative parameters to coordinate post-embryonic morphogenesis in the eye of fish" for peer review at eLife. Your article is being evaluated by Marianne Bronner as the Senior Editor, a Reviewing Editor, and two reviewers.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond within the next two weeks with an action plan for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

Summary:

In this paper, Tsingos et al. use imaging and modelling approaches to understand how an organ (the eye) can continually grow throughout an organism's life while maintaining a precise morphology. They identify a novel interplay between neural retina and retinal pigmented epithelium cells, whereby the latter divide more stochastically. They further identify orientated cell divisions as critical in regulating the organ growth. They effectively utilise modelling to demonstrate how these different modes of cell differentiation and division can result in coordinated continual organ growth.

Essential revisions:

1) A first major comment is on fundamental feedback modes. The authors state that the feedback mechanisms coordinating growth of all tissues could be wired in "two ways: either the tissue of interest acts upstream to induce growth of other tissues, or, vice versa, the tissue of interest lies downstream of growth cues from another tissue in the organ", named respectively "inducer growth mode" and "responder growth mode". It is unclear upon what evidence this dichotomy bears. Specifically, in comparison to these extreme cases, in how far would the model be able to distinguish between more intermediate scenarios, where growth is regulated both by extrinsic and intrinsic cues, or both tissues serve as inducer and responder at the same time?

2) The impact of this study is limited by a lack of statistical and biophysical rigor. The authors make experimental observations that are, in principle, quantitative. However, the predictions made by the computational model are only qualitatively compared to experimental data. In the revised version of the manuscript the authors should (a) employ statistical tests and calculate p-values to quantify the statistical significance of biological effects, (b) quantitatively compare experimental observations (e.g. clone fragment size distributions or similar) with computational predictions, and (c) employ appropriate statistical criteria to evaluate whether the model is quantitatively able to distinguish between different biological scenarios.

3) On the biophysical side, the computational model is based on a rather complex set of rules which depend on a large number of parameters. Many of these parameters are fixed based on experimental measurements, but some, in particular those changed between the two biological scenarios, do not have a clear biophysical interpretation or are adjusted "empirically". For example, the probability of division for virtual stem cells is set to be 1/26 per hour. It is unclear how this value is chosen. It is also inadequately explained how the minimal displacement threshold, µ, is "empirically determined". It has to be shown that the main conclusions of this work do not sensitively depend on the specific values of parameters that are not experimentally measured.

4) The concept of stochasticity in proliferation is used in a confusing way throughout the text. In subsection “Fundamental feedback modes of organ and cell growth impact on clonal patterns”, the authors imply that the responder growth mode leads to higher variability of cell cycle timing in individual cells. As cell divisions in both growth modes are, by the definition of the model, stochastic the authors should use more appropriate statistical wording for this finding (e.g. variance of cell cycle times). In addition, this result should be quantitatively demonstrated based on simulation data. Further, the authors do not comment on the biophysical origins of the observed differences in the variability of cell cycle timing. Are they associated with fluctuations in cell density?

5) (Statistics) The results of Figure 1E are promising but the analysis can be strengthened. Presentation of a single image is not sufficient to convince the reader that RPE ArCoS frequently have more irregular shaped clones. Quantification of the clonal topology across a number of samples is necessary to provide meaningful support. A similar critique holds for Figure 2D' – superficially, the clusters do not look that different and better quantification is needed to backup such statements (subsection “Fundamental feedback modes of organ and cell growth impact on clonal patterns”).

6) The description of the model can be improved. Details are too vague. For example, I found the sentence "We took advantage of this…" (subsection “A minimal complexity 3D agent based model of retinal tissues”) unclear – what exactly is helping and why? It is not obvious to me how you go from discussing the multi-layered columns of the progeny to simplifying model complexity. Further, clearer justification needs to be given why an effectively hard sphere model is a reasonable approximation to an epithelial tissue.

7) The authors argue that δ = 0.4 is the right threshold for overlap. It would be helpful to more explicitly elucidate what happens to the system as δ is increased or decreased – this would provide a clearer picture of how the parameter δ regulates the model output.

8) The nomenclature for the ratios is incorrect. Typically, a colon ": " is used to represent a ratio, not an "=" sign. This makes the results in subsection “NR stem cells undergo radial divisions at the rate predicted by shape regulation” hard to read and this needs to be reworked to improve clarity.

9) Subsection “NR stem cells undergo radial divisions at the rate predicted by shape regulation – the ArCoS width (which implies a distance) is given as an angle. It is either the angular extent (or similar) or give the arc length. Relatedly, I cannot believe that the experiments are measured to a hundredth of a degree (4.87º). Give experimental measures (here and elsewhere) to an appropriate level of accuracy (in this case, likely 5º).

10) Subsection “NR stem cells undergo radial divisions at the rate predicted by shape regulation”. The authors note that simulations with "ideal" division axis match the experiments. What happens at more intermediate levels – i.e. how robust is the system?

11) Figure 6E (subsection “Local biases in ventral NR stem cell divisions influence retinal topology”) does not seem to be present.
