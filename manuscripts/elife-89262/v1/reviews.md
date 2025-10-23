# Peer review - Round 1

Editors:
- Daniel Henrion, University of Angers France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.89262.3.sa0](https://doi.org/10.7554/eLife.89262.3.sa0)

The authors used an appropriate micro-engineered experimental model of angiogenesis coupled to mathematical model to study the early steps of the angiogenic sprouting. To this end, the authors developed a convincing model to predict how VEGF activates Delta-Notch signaling. The work affords important new insight into the complex processes involved in the onset of angiogenesis.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89262.3.sa1](https://doi.org/10.7554/eLife.89262.3.sa1)

The authors succeeded in establishing experimental and mathematical models for the formation of new blood vessels. The experimental model relies on temporal imaging of multilcellular projections and lumen formation from a single blood vessel embedded in an engineered extracellular matrix. The mathematical model combines both discrete and continuum elements. It would be helpful to understand how the authors came up with phenotypic classes for analyzing their live imaging data. On the modeling side, it would be useful to see whether the claims about Turing patterns could be supported by either a mean-field model or a more thorough parametric analysis of the discreet continuum model. The authors did a good job in comparing their VEGF/Notch mechanism to the EGF/Notch vulval patterning mechanism in C. elegans. The authors might want to look into the literature from studies of the tracheal patterning system in Drosophila when the combined actions of the FGF and Notch signaling specify tip and stalk cells. The similarities are quite striking and are worth noting.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.89262.3.sa2](https://doi.org/10.7554/eLife.89262.3.sa2)

Summary:

In this manuscript, the goal of the authors is to understand the process of mature sprout formation from mini-sprouts to develop new blood vessels during angiogenesis. For this, they use their earlier experimental setup of engineered blood vessels in combination with a modified spatio-temporal model for Notch signalling. The authors first study the role of VEGF on Tip (Delta-rich) and Stalk (Notch-rich) patterning. The Tip cells are further examined for their space-time dynamics as Mini-sprouts and mature Sprouts. The Notch signalling model is later supplemented with a phenomenological _random uniform model_ for Sprout selection as a plausible mechanism for Sprout formation from Mini-Sprouts. Finally, the authors look into the role of fibronectin in the Sprout formation process. Overall, the authors propose that VEGF interacts with Notch signalling in blood vessels to generate spatially disordered and co-localized Tip cells. VEGF and fibronectin then provide external cues to dynamically modulate mature Sprout formation from Mini-Sprouts that could control the location and density of developing blood vessels with a process that is consistent with a Turing-like mechanism.

Strengths and Weaknesses

In this manuscript, work motivation, problem definition, experimental procedures, analysis techniques, mathematical methods (including the parameters), and findings are all presented quite clearly. Moreover, the authors carefully indicate whenever they make any assumptions, and do not mix unproven hypothesis with deduced or known facts. The experimental techniques and most of the mathematical methods used in this paper are borrowed from the earlier works of the corresponding authors, and thus are not completely novel. However, the use of these ideas to provide a simple elucidation of the role of VEGF and fibronectin in Sprout formation, in an otherwise complex system, is very interesting and useful. Some of the data analysis methods presented in the paper - (i) quantification of Tip spatial patterns (Fig. 3) and (ii) Sprout temporal dynamics using Sankey diagram (Fig. 4) - seem quite novel to me in the context of Notch signalling literature. Similarly, the authors also provide a new mechanism (VEGF) to obtain disordered Delta-Notch patterning without explicitly including _noise_ in the system (Fig. 2 and Fig. S1). The authors also systematically quantify the statistics of spacing between the Sprouts and show that the Sprouts have a tendency to be away from each other, something that they could also partially recapitulate by additionally including a novel _random uniform model_ for Sprout selection (Fig. 5). Although the association between fibronectin and angiogenesis is known in the literature, in this manuscript, the authors could clearly demonstrate that fibronectin is present in high and low levels, respectively, around Sprouts and Mini-sprouts (Fig. 6). A combination of these findings could then motivate the authors to hypothesize, as mentioned above, a Turing-like mechanism for Sprout formation, something that I find interesting.

Although I find the relative simplicity of the experimental system and theoretical model and the clear findings they generate appealing, some aspects raise a few questions. The authors experimentally find 20 +- 0.08 percent of Tip cells in the model blood-vessels that is consistent with the salt-and-pepper pattern seen in Notch signalling model (~25 %). However, it is not clear to me if the reverse is true, i.e., 25% of Tip cells automatically imply a salt-and-pepper pattern - the authors do not seem to provide a direct experimental evidence. Furthermore, the authors use their Notch signalling model on a regular hexagonal lattice, but there is a large variability in the cell sizes (Fig. 3) in the experimental system. Since it is observed in the literature that signalling depends on the contact area between the neighbouring cells, it is not clear how that would affect the findings presented in this paper. Similarly, since some of the cells are quite small compared to the others, I worry how appropriate it is to express the distance between the Tip cells in terms of _cell numbers_ (Fig. 3). Regarding Sprout classification, as per Table 1, a bridge of two cells is formed as per early-stage-I mechanism for Sprout. On the other hand, the entire data interpretation of experiments seems to be based on early Stage II and matured stage in that same table (also Figs. 3 and 4) in which only one Tip cell seems to be counted per mature Sprout. However, if some Sprouts are formed via early stage-I mechanism, a projection in 2D for analysis would give a count of __two__ adjacent Tip cells, but corresponding to a __single__ Sprout. It could be possible that the presence of such two-cell Sprouts affects the statistics of inter-Sprout distances (Fig. 5). Finally, I find the proposed mechanism of Sprout formation dynamics to be somewhat unsatisfactory. Other than the experimental evidence regarding the spacing of Sprouts and the fibronectin levels around Sprouts and Mini-sprouts (Figs. 4 and 5), there is very little evidence to support the hypothesis about a Turing-like mechanism for Sprouting. Moreover, it seems to me that Turing patterns can appear in a wide variety of settings and could be applied to the current problem in an abstract manner without making any meaningful connections with the system variables. Also, from a modeling point of view, cell migration and mechanics, are expected to take a major part in Sprout formation, while cell division and inclusion would most likely influence Tip-Stalk cell formation. However, it seems that in the present work, these effects are coarse-grained into Notch signalling parameters and the Sprout selection model, thus making any experimental connection quite vague.

Overall Assessment

I feel that the authors, on the whole, do achieve their main goals. Although I have a few concerns that I have raised above, overall, I find the work presented in this manuscript to be a solid addition to the broad field of collective cell dynamics. The authors use well established experimental and mathematical methods while adding a few novel analysis techniques and modeling ideas to provide a compelling, albeit incomplete, picture of Sprout formation during angiogenesis. While the direct application of this work in the context of angiogenesis is obvious, the broad set of ideas and techniques (discussed above) in this work would also be useful to researchers who work on Notch signalling in morphogenesis, collective cell migration, and epithelial-mesenchymal-transition.
