# Peer review - Round 1

Editors:
- Pierre Sens, Institut Curie, PSL Research University, CNRS France

Reviewers:
- Igor S Aranson

## Review text

DOI: [10.7554/eLife.46842.sa1](https://doi.org/10.7554/eLife.46842.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Bridging the gap between single-cell migration and collective dynamics" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

All three reviewers shared concerns that the model was insufficiently connected to real data, and that the novelty of the model with regards to existing models of the same flavour (cellular Potts model) where not sufficiently highlighted.

They all agreed that providing a model that is applicable to both single cell and multi-cellular phenomena is a worthwhile endeavour to "bridge the gap" between single and collective cell migration. However, the single cell part lacks comparison with real data and proposal for experimental check of falsifiable predictions. The multi-cellular aspect was unanimously found more interesting/novel, but much less developed. Explicit suggestions by reviewer #3 on improvements/extensions of the multi-cellular part will likely require quite a bit work and time to be implemented.

Reviewer #1:

This paper describes a Cellular Potts Model for single and collective cell migration.

Single cell motility reproduces the crescent shape of keratocyte-like crawling cells and gives prediction regarding cell size and polarisation.

At the multicellular level, the model reproduces collective rotation of cells confined in circular domains. The authors have discussed this behaviour in a previous paper (Segerer et al., 2015) using a model which I believe is very similar to the present one (or exactly the same?), but which is not detailed in Segerer et al., 2015. Here, there they find an interesting behaviour, with an optimal ratio of polarizability to contractility for persistent collective cell rotation.

Finally, they study the tissue-level dynamics of a typical "wound-healing" assay, and study motility vs. cell proliferation dynamics.

This paper is study situations of direct experimental and biological relevance and reproduces a number of expected results. This is a valuable addition to the already fairly large body of work on the modelling of cell motility. Furthermore, the same model is applicable to single cell motility but also to collective motility in multicellular systems, which is quite interesting.

On the other hand, I found the model quite complicated, with a number of ad-hoc ingredients. This might be reasonable, since the experimental system is complicated as well, and the ingredients are based on known physiological factors, but the extent to which their results are universal is unclear, and little effort is made to address this point.

The comparison with experiments remains qualitative at best, or even anecdotal. For instance, the recent shape of single migrating cell is universally obtained from a number of models. On the other hand, they predict that cell must be large enough to polarise and move persistently, which is highly non-trivial (may be even counter-intuitive?) and could be a crucial test of the model as compared to others but is not discussed further.

I think going beyond these limitations would probably require quite a bit of additional work. The paper as it stands is a very valuable piece of work but might bring more questions than it gives answers. I would recommend enhancing the discussion on the universality of the model and reinforce the discussion of the prediction is relation to experimental finding, and if possible, make that discussion more quantitative.

Reviewer #2:

There is nothing really wrong with this paper and it would make a fine submission to PLoS Computational Biology. Essentially the authors introduce a more complicated version of the cellular Potts model (CPM) to study individual and collective cell motility. The original CPM had several clear deficiencies involving the lack of active cytoskeleton-based driving and the insufficient treatment of adhesion. There have been some remedies for these deficiencies already published but on the whole the model proposed here seems to be a good step forward.

But I do not see sufficient scientific findings that have emerged so far from this new model to warrant acceptance of this paper for eLife. The results on single cell motion are not actually compared to any data, for example to keratocyte shapes versus parameters as available from the Theriot lab. Also, although the authors claim that at small R there is a lack of coherence of active protrusion across the cell front (Figure 3D), when this happens in actual cells such as Dictyostelium we see much more pronounced stochasticity involving pseudopods of a characteristic scale; as far as I can tell this does not happen in this model. The fact that cells exhibit persistent random walks with correlation times that depend on various parameters is hardly surprising. Other issues regarding single cell motion, such as guidance in the presence of gradients either chemical or mechanical are not presented at all.

Again, I saw nothing strikingly different from previous results for rotating clusters and again no comparison to any experimental data. The model seems to make reasonable predictions but this is not enough for acceptance given the previously published work on this situation.

For tissues the case is somewhat better. Some of the ideas and results here recapitulate what has been seen in other models; this holds for example for the density structure of the population, which in this paper is based on a division rule that directly mimics those used in earlier works. Other aspects appear more novel, such as the reproduction of some the findings regarding wave-like behavior in expanding tissues. But again, this agreement stays at the purely qualitative level, leaving the reader with no specific predictions which could be used to test the validity of the proposed mechanism.

Finally, it was almost impossible to understand the presentation of the model in the main text, with all sorts of symbols and rules appearing out of nowhere. The appendix remedies this problem, but it would almost be better to just describe the pieces qualitatively in the main text instead of undertaking a valiant but in the end failed attempt to include some detailed formulas. In passing, Figure 1 seems to be missing some subfigures.

Reviewer #3:

The manuscript features a coarse-grained description of cell and tissue migration based on the generalization of the cellular Potts model. I think the work contains enough new results to justify publication in eLife. However, prior to the publication, the following points need to be addressed. My main concern is that the potential of the computational model is not fully explored.

1) Computational model. The description of the model is rather comprehensive and clear. However, it is necessary to highlight the differences between the current model and earlier CPM approaches to cell motility, e.g. in Kabla, 2012, Doxzen et al., 2013. What is the main difference that enables bridging the single-cell and collective dynamics?

2) Single cell migration. The computational model demonstrates that the cells can polarize and adopt a crescent shape. However, recent experimental studies predicted a phenotype change for the same cell line: a transition from migration to rotation: (i) Lou et al., 2015. (ii) Raynaud F. et al., 2016. This transition was captured in the framework of the phase-field model for slightly higher rates of actin polymerization, Reeves et al., 2018. I am wondering if the CPM model can also capture this transition for stronger driving parameters.

3) The tissue level dynamics. This part of the work is possibly the most innovative and crucial. However, exploration of the tissue dynamics in this section is rather brief. Certainly, the reproduction of the X-pattern is interesting. But many other relevant phenomena can be easily investigated with this method, e.g. instability of the growing front of the cells. Many experiments show that in the course of wound healing, the cell front exhibits a sort of fingering instability. Is this phenomenon captured by the model or the front always remains flat? Another interesting issues are the change of topology and stress distribution at the onset of confluence, and how the number of neighbors changes in the process of cell migration. The CPM model can be contrasted for example to active vertex model where the topological changes are not allowed, DL Barton, S Henkes, CJ Weijer, R Sknepnek, PLoS computational biology 13 (6), e1005569.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "Bridging the gap between single-cell migration and collective dynamics" for further consideration by eLife. Your revised article has been evaluated by Naama Barkai (Senior Editor) and two reviewers, one of whom is a member of our Board of Reviewing Editors.

The reviewers found the paper much improved, in particular regarding the way the model is explained and justified. There are some remaining issues that need to be addressed before acceptance, as outlined below:

– The model for cell division (subsection “Tissue growth by cell division”) should be justified better. Division is said to occur stochastically when the cell size reaches a threshold. Here, the size refers to the spread area, not to the cell volume. Why should division be triggered by an increase of spread area. Single cells actually round up and detach from the substrate before dividing. Are there experimental indications that cell division in an epithelium is triggered by an increase of cell area?

– Blebbistatin is claimed not to affect cell shape of speed (subsection “Cell persistence increases with polarizability”), which is explained by it affecting polarizability and contractility to the same extent. This argument is not entirely convincing. First, it is not clear why blebbinstatin should reduce protrusive force due to actin polarisation. One could make the counter argument that myosin contraction reduce protrusion forces by increasing actin retrograde flow, and blebbistatin-treated cells are often seen to spread faster than intreated cells. Second, the effect of blebbistatin on single cell motility is very diverse, and highly depend on the cell type. Both enhancement and decrease of the migration speed are reported in the literature. This paragraph should not give the feeling that the effect of blebbistatin on motility is universal.

– Regarding the correlation between cell shape and speed (subsection “Cell persistence increases with polarizability”), the model seems apt to capture the behaviour of keratocyte (fast and crescent shaped), but many cell types are actually elongated in the direction of their motion. The is presumably due to polarised protrusion forces along the direction of motion with slow cell detachment at the back. While one can hardly expect a single model to capture all phenotypes, could the author speculate and comment why their model is more appropriate for the crescent-shape phenotype.

– Figure 3F suggest two possible correlation between cell shape and direction of motion: the crescent shape, where cell is elongated perpendicular to its direction of motion, and a cell aligned with the direction of motion. This is not discussed in the text, which is unfortunate. What factor determines in which situation the system is, and how does this affect speed and persistence?

– The discussion of tissue level dynamics uncovers several regimes of growth: i.e. driven by the motility of the cells at the tissues edge, or by cell division. It would be interesting to discuss the extent to which these two regimes could be obtained from a continuous model with an effective viscosity (cf. Appendix 1—figure 3) and a driving force due to motility at the edge or a pressure coming from cell division. Such an effective continuous model should be attempted and compared to the numerical results. For instance, judging from Figure 5, the cell front expands almost linearly in time for motility driven, and may be quadratically in division driven. Could such law be discussed and obtained from simple continuous models?
