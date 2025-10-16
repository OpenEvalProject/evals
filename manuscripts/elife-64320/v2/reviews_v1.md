# Peer review - Round 1

Editors:
- Job Dekker, University of Massachusetts Medical School United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64320.sa1](https://doi.org/10.7554/eLife.64320.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The work describes a simple theoretical model for enhancer action that explains several major controversies in the field of long-range gene regulation and the role of topologically associating domains and insulating boundaries in modulating enhancer-promoter interactions. Further, the model makes predictions that be experimentally tested. This is valuable for the field of gene regulation.

Decision letter after peer review:

Thank you for submitting your article "How subtle changes in 3D structure can create large changes in transcription" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Job Dekker as the Reviewing Editor and Reviewer #3, and the evaluation has been overseen by Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Katie S. Pollard (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary:

The work describes a simple theoretical model for enhancer action that explains several major controversies in the field of long-range gene regulation and the role of topologically associating domains and insulating boundaries in modulating enhancer-promoter interactions. Further, the model makes predictions that can be experimentally tested. This is valuable for the field of gene regulation.

Essential revisions:

All three reviewers agreed the work addresses a major question in the field but also raised important issues that should be addressed. These primarily revolve around how the model is described, and the extent to which the full parameter space is explored. Further, the authors have not explored alternative models which would help clarify how surprising and robust their results are. There is also an opportunity to emphasize that the proposed model is not necessarily absolutely correct, but one of many plausible models that can produce a non-linear relationship between genome structure (enhancer-promoter contact) and transcription. Any thoughts on other models that could generate similar dynamics would be a useful discussion point.

1. The presentation of the model is unclear. It is currently present in the text, lines 110-122, in pure qualitative description. Authors define only rates in the text; definitions of other model parameters are not present. For example, E and a are not specifically defined in the text or Methods section. Since both terms "enzyme" and "enhancer" are being used and in fact "enzyme tagging" and "enhancer tagging" occur simultaneously in the model, it is not possible to say for sure when do authors call which one in the model and thus the methods section can be interpreted in different ways. Moreover, the cartoon is missing a legend confirming, which molecular player is which. The figure caption mentions only green triangles being the tags, but no other parts of the cartoon are being explained. Taken together, this makes it very difficult to verify the mechanics of the model.

– Given its centrality to the manuscript, we recommend describing the overall strategy in more detail in Results. For example, at line 124 (Pg. 4) the authors could talk about how the simulations are done, including where the variability comes from (e.g., random starting conditions vs. probabilistic events vs. different parameters).

– – The authors should provide a detailed technical description of their model directly in the text, including description of their parameters, list their constitutive equations and identify all parameters in their cartoon Figure 1C.

– Axes labels in all figures should be expressed in the parameters/variables of the model (as in Figure 6C-D) directly connecting to inputs/outputs of the model.

2. In the Methods section, it appears that in lines 577-580 of the model description, the mass is not conserved. This issue is critical to address, because when mass is not conserved the model can not be physical.

3. Xiao et al. make several key assumptions to dramatically simplify their model. Namely, it is assumed that promoter modification and transcription are equivalent and that enhancer-promoter contact influences transcription instead of transcription influencing structure. Steady-state equilibrium must also be assumed. It would be helpful if the authors explicitly stated these assumptions and provided references to support their being reasonable.

4. For clarity, it would be helpful to discuss model parameters in greater detail. First, we suggest noting which parameters shift the location of the curve and which increase the steepness of the curve. Second, we recommend including a phase diagram exploring when sigmoidal behavior and any other key model predictions arise across parameter space. In what circumstances does hypersensitivity or time lag emerge? The authors demonstrate that a narrow set of parameters is sufficient to produce a super-linear relationship between enhancer-promoter contact and transcription in Figure 6. One potential dilemma is this model's ability to explain many experimental observations by indicating that minimal changes all occur in the sub-linear regime while observable changes occur in the super-linear regime. Given that one needs specific parameters to replicate an example of the hyper-linear regime (including at least three degrees of stimulation and increasing stimulation of the successive states), it could be valuable to demonstrate how large the plausible parameter space is. Without an exhaustive search across the space of minimal parameters, it is not clear when this property emerges or how common it is within the full parameter space. The authors could vary model parameters and plot a grid visualizing behavior (e.g., steepness of the curve or Hill coefficient).

5. The authors observe hysteresis in median transcription rate as a function of enhancer contact frequency. However, the presented violin plots suggest a presence of two states, one with low and one with high transcription rates. In the intermediate regime of enhancer contact frequency, where authors report hysteresis, the violin plots show bimodal distributions suggesting coexistence of these two states. This would suggest that the system exists in and switches between two distinct states with a discontinuous transition, instead of a continuous hysteretic behavior as suggested by the median behavior.

6. There is also an opportunity to emphasize that the proposed model is not necessarily absolutely correct, but one of many plausible models that can produce a non-linear relationship between genome structure (enhancer-promoter contact) and transcription. Any thoughts on other models that could generate similar dynamics would be a useful discussion point. There are parallels to both sigmoidal dose-response curves, where drug concentration is plotted against response, and transcription factor binding curves, where free ligand concentration is plotted against the fraction bound. We recommend providing background context on these types of models or the Hill equation to illustrate why non-linear behavior is or is not surprising given the proposed model.

7. It is not totally clear why the authors decide to call their proposed approach the futile cycle model. There are similarities to other well-known models in biochemistry and biophysics that should be noted. It might make sense to simply call this a mechanistic model of cooperative promoter activation. If the authors stick with "futile cycle", the relationship between promoter activation through tags and metabolic signaling should be described in more detail.

8. At the beginning of the Discussion section authors state they will propose future experiments in each section. However, in some of the sections it is not clear what specifically authors are proposing. These suggestions should be made clearer.

9. If I understand the model correctly, the non-linearity arises because of the increase rate of tag addition when tag is already present. The authors then speculate histone modifications can be one such tag. However, there is only so many sites of modification at a promoter. Can the authors analyze how the possible range of tag densities affects performance of the model? Is the range required biologically plausible?

10. Can the authors do more analysis to explore how rapid changes in gene expression may occur (e.g. upon signaling a gene may go up within minutes)? How much more frequent does the E-P interaction need to be for rapid switch to the active promoter state? Can the authors do an analysis where they change the rates of the futile cycle upon some signal: at what time scale does transcription then change (keeping E-P frequency the same)?

11. Due to the lack of description, in many sections it is not clear what are the specific inputs and outputs of the model (e.g. Figure 2).

12. The Methods section describes the chemical kinetics of the suggested reactions and the insulation score calculations. But it is not clear how do these inform each other, how are contact-frequency maps chosen/computed and cross-referenced with the local E-P kinetics?

13. In 587-588, the index of k is 2(n+1), which equals to 2n+2, but then in the next line the following assumption is made 2n+1 → n+1.

14. The authors make assumptions that their kinetic considerations hold for n>2. What is the evidence?

15. The language of the paper is often not technically precise with qualifiers missing, which could lead to ambiguities and misinterpretations. Here are some examples:

p. 1, line 10, "difference in contact across TAD borders is usually less than twofold";

p. 1, line 17, "results from recent cohesion disruption";

p. 2, line 71, "A simple model of hypersensitivity to changes in contact frequency".

16. On p. 13, line 483, authors define Ostwald ripening as given by weak multivalent interactions; however, Ostwald ripening is a thermodynamic process. In addition, they propose that liquid condensates become larger due to Ostwald ripening, but there are also other processes that may occur, such as coalescence of condensates, which would also lead to larger condensates.

17. An alternative explanation for TAD-specific enhancer action is that an E-P interaction within a TAD (between two convergent CTCF sites), one that is brought about by extruding cohesin, is not equivalent to an interaction that occurs between two loci on either side of a CTCF site and that can be a random collision that is not mediated by extruding cohesin. In other words, two interactions can be of the same frequency but can be of a very different molecular nature. I agree that this model would not explain the results of the experiment where cohesin is acutely removed.

18. In the beginning of the introduction the authors introduce TADS. I recommend that the authors present this in a more nuanced way: compartment domains also appear as boxes along the diagonal, an issue that has led some in the chromosome folding field to be confused. This reviewer believes TADS are those domains that strictly depend on cohesin mediated loop extrusion, whereas compartment domains are not. If the authors agree, perhaps they can rewrite this section?
