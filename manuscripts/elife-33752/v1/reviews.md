# Peer review - Round 1

Editors:
- Laura Colgin, The University of Texas at Austin, Center for Learning and Memory United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33752.035](https://doi.org/10.7554/eLife.33752.035)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A Model of Spatial Memory and Imagery – From Single Neurons to Cognition" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Frank as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This paper describes a model that proposes a framework to explain how multiple, highly complex regions interact to produce egocentric and allocentric representations of space. Although all reviewers found the model to be interesting and novel, they also agreed that the Results, Materials and methods, and rationale for the model were often not presented in a clear and concise manner that would be optimal for a broad readership. Reviewers also felt that the simulation movies were insufficient to demonstrate the importance of the model and request a number of essential revisions, including incorporation of clear performance goals for the model, together with appropriate quantitative measures.

Essential revisions:

1) A primary shortcoming is that the model is not used to simulate any specific behavioral tasks. Instead, after describing the architecture, the paper presents a series of several simulations (depicted by figures and videos) to demonstrate examples of neural population activity (over time periods lasting tens of seconds) during a few selected types of navigational behavior. These example simulations do not provide adequate support for strong claims made in the Discussion section, where it is argued that the model accounts for a wide range of findings including position specificity in visual object memory (Hollingworth, 2007), impaired episodic memory resulting from Papez circuit lesions (Delay and Brion 1969), neural activity seen during imagery for scenes in the MTL, retrosplenial cortex and precuneus (Burgess, Maguire et al., 2001; Hassabis et al. 2007; Schacter et al. 2007), and 'some aspects' of 'scene construction' and 'episodic future thinking' (Schacter et al., 2007; Hassabis et al., 2007; Buckner 2010). To support such claims, the model should more faithfully reproduce experimental designs from these prior studies (as is, there does not seem to be any quantitative metric by which these broad claims can be evaluated). It is also implied that the model accounts for "trace cells" that fire when the agent visits the prior location of a missing object (Tsao et al., 2015), and although trace-like activity is shown in some example simulations, it is not specifically stated which neural population in the model would correspond to trace cells, nor are simulated trace cell firing rate maps presented. It is additionally claimed that the model accounts for preplay and replay activity of place cells, but it appears that simulated preplay and replay events do not occur on a compressed time scale in the model as they do in real rodents, which is not addressed. In other words, the heavy reliance on qualitative (rather than quantitative) performance assessments make it difficult to offer anything more than a subjective evaluation of the model's capabilities. A more objective evaluation might be possible if the authors run more simulations to quantitatively compare simulated vs. real neural activity (or simulated vs. real task performance), explore how the model's performance degrades under realistic noise or uncertainty conditions, etc.

2) Several key mechanisms – such as sequential shifting of attentional focus (which is essential for solving the place-object binding problem), neuromodulation (which allows the model to transition between sensory processing and mental imagery modes), and population activity in the grid cell map (which is essential for generating preplay/replay trajectories) – are not explicitly simulated by the model. Rather, these signals are provided "for free" as inputs to the network. When reciting the list of phenomena that the model can explain (see prior point), the authors should take care to include only phenomena that fall within the purview of what is actually being simulated by the network, rather what is being provided for free.

3) The depiction and explanation of BVC and PWb data (initially shown in Figure 2A2, C1, and C2 and also described in subsequent figures) is unclear. Why are small receptive fields shown close to the agent in Figure 2A2? What does this mean? In the Video 1, receptive fields do not appear to get smaller or bigger as the agent moves around. Are the cells with receptive fields close to the agent the ones that fire at the actual boundaries, not a distance away from the boundaries? If not, in Figure 2C1, why are BVCs shown to be firing, presumably at the north and east boundaries of the environment, when the agent is in the center of the environment (i.e., not in the boundary)? Why are so many BVCs firing at the same time when the agent is in a particular location? Are these different cells that fire at different distances from the boundaries? Figure 2A2 is described as showing receptive fields for BVCs, but these receptive fields are usually more rectangular in shape, whereas they are depicted as circular here. In "bottom up" mode (e.g., Figure 5, top) it appears that only BVCs encoding boundaries ahead of the animal (those in the visual field?) are active. Is this consistent with the firing of real neurons (such as border cells)? Is there any evidence that real BVCs are active only when a rodent faces toward but not away from their coded boundary?

4) The authors show a schematic of their model in Figure 4, which includes top-down and bottom-up connections between different brain areas. Lacking from the paper are multiple citations to anatomical studies that demonstrate that these connections are realistic (e.g., Jones and Witter, 2007, for projections from retrosplenial cortex to deep layers of entorhinal cortex). For example, has it been shown that the entorhinal cortex projects back to the retrosplenial cortex?

5) In Figure 7D, why isn't anything activated for the new object?

6) The authors go to great lengths to realistically model MTL activity based on rodent literature. However, it was not clear how the model relates to rodent literature regarding parietal coding (e.g. Harvey, Coen and Tank, 2012; Raposo, Kaufman and Churchland, 2014; Whitlock et al., 2012) and retrosplenial coding (Vedder, Miller, Harrison, Smith, Cerebral Cortex, 2017; Alexander and Nitz, 2017; Alexander and Nitz, 2015). Can the model account for the type of coding observed in navigating rodents in these regions? Or are there specific predictions the model can make about what would be observed or how these types of observed neural codes can be interpreted in the context of spatial cognition?

7) In some places, terms are used that assume prior knowledge to a degree that can make the paper difficult to parse. Some examples include 'gain-field circuit' (Introduction), the current model as an extension of the 'BBB model' (Introduction), 'heuristically implemented', 'mock-motor-efference'. Terms like this could use additional (but very brief) explanation when introduced.

8) The paper can be a bit long in places – particularly the sections on preplay and replay.

9) Figure 4: was activity from place cells to grid cells considered?

10) The presence of object specific coding appears to be a 'strong prediction' of the model, as object coding reported thus far is minimally selective for specific objects. The authors detail potential places where this activity might be found but they may want to consider that these types of representations lay outside the cortex or emerge as a population level representation (i.e. would not be observable at the level of single cell tuning curve responses).

[Editors’ note: this article was subsequently rejected after the authors submitted their revisions but they were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "A Neural-Level Model of Spatial Memory and Imagery" for consideration by eLife. Your article has been reviewed by one peer reviewer, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

We regret to inform you that your work will not be considered further for publication in eLife.

After consultation, we feel that the paper remains too cumbersome for a general audience, and some points remain unclear.

Reviewer #3:

In this paper, Bicanski and Burgess present a network model to propose how multiple populations of spatially tuned neurons are functionally interconnected with one another to form a spatial memory network with multiple capabilities.

A core feature of the model is that it proposes how bidirectional transformations between the egocentric and allocentric reference frames might be performed by networks in the retrosplenial cortex. The paper ambitiously attempts to demonstrate numerous capabilities for the model, such as mapping a familiar environment, learning the locations of unique landmark objects in such an environment, detecting novelty when changes occur in an environment, and simulating effects of brain lesions upon memory and navigation. The paper incorporates 13 videos, 13 figures, and 18 methods equations. Despite its length (nearly 60 pages), the paper does not provide enough detail for readers to fully understand some key aspects of the model (see below). This should not be interpreted as an entreaty to make the paper even longer. Rather, the paper should probably be split up into at least two publications, each dedicated to exploring specific capabilities of the model with more clarity and depth.

As noted in the prior review, simulations of mental navigation and route planning do not seem to be rooted in the model's core ability to perform bidirectional egocentric / allocentric transformations. Instead, it is the addition ("for free") of a grid cell network connected to place cells endows the model with this capability. How does the egocentric / allocentric transformation network contribute to the mental navigation and route-planning process? What is the functional purpose for transforming allocentric replay events back into the egocentric coordinate frame to generate imagery? The grid cell driven simulations do not even appear until the subsection “Grid cells and mental navigation (Simulation 4.0)”, and given how information dense the preceding pages are, perhaps the addition of the grid cell network and accompanying simulations might be better suited to a second paper, dedicated more specifically to the topic of route planning?

Another problem raised in review, which has not been adequately addressed, is that the sequential shifting of attentional focus is not explicitly simulated by the model, and not explained fully enough for readers to comprehend how this process contributes to the simulation results. To solve the problem of binding each object or boundary's location to its identity, the model adopts a sequential shift of attention strategy. If I understand correctly, each population of boundary (BVC) or object (OVC) cells is activated one at a time in conjunction with its corresponding boundary (PRb) or object (PRo) identity cell. The length of each attentional cycle is stated to be 600 time units. How does information about multiple objects and boundaries get integrated across multiple attentional cycles to form a stable and non-fluctuating representation of the environment as a whole? Do PCs have slow activity decay kinetics that can span multiple attentional cycles? How is such temporal integration accounted for in analyses like that shown in Figure 8, where momentary "snapshots" of population vectors are being correlated with one another across encoding vs. recall? Because of the sequential attention mechanism, one would expect that an incomplete representation of the environment (i.e., just one object and one boundary) would be active at any given time. So I don't quite see how it is possible to use an instantaneous snapshot of the population vector to perform these correlation analyses, unless the snapshot is being taken at the end of some temporal integration process that spans multiple attention cycles?

Finally, since the heart of the model is the retrosplenial transformation network, it is a bit surprising that no simulation results are shown to demonstrate the predicted firing properties of retrosplenial neurons that perform the egocentric / allocentric transformation (in either direction) during imagery and recall. Do any testable predictions for unit recording studies arise from the firing properties of these model neurons? If so, then it seems like they should be included in the paper.

In summary, there are some innovative features of this model that would of interest to the research community, but the format of the paper (including its length) may not be best suited for publication in eLife. The authors might wish to consider splitting the paper up into two publications (e.g., one on coordinate transformation, and one on mental navigation and route following) so that some of the missing details of the model can be more thoroughly described without adding even more to the current manuscript's excessive length.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "A Neural-Level Model of Spatial Memory and Imagery" for further consideration at eLife. Your revised article has been favorably evaluated by Michael Frank (Senior Editor), a Reviewing Editor, and one new reviewer.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer #1:

In the revised manuscript, the authors have done a lot of work to respond to previous criticisms, including adding new results to respond to the initial criticisms.

There is much value and novelty in this model, which provides a potential explanation of how egocentric and allocentric representations of space are reconciled. Also, as the authors point out in their appeal, the excessive length of the manuscript is due to results that were added to satisfy the original reviews. I feel confident that the specific feedback provided below will allow the authors to clarify points that remain puzzling.

1) I didn't really understand what the "transformation sublayers" are. Are they between areas or in the retrosplenial cortex part of the model? How are they different from "individual sublayers" (subsection “The Head Direction Attractor Network and the Transformation Circuit”, second paragraph)?

2) In all of the figures and videos involving the top-down mode/recall/imagery, why does firing occur for all directions of boundaries in PWbs and BVCs?

3) In Figure 12A, why are OVCs to the east firing when object 2 is in the northeast of allocentric space?

4) In Video 8, I don't understand at time = 1.67 seconds how the OVC pattern matches that during perception for object 2. It looks like object 1. OVC activity at NW at 1.67 seconds looks the same as OVC activity at NW at 6.52 seconds, the time at which the text states that activity matches that during perception for object 1. Related to this, in Video 12, at time = 11.52 s, OVC do not seem to be representing object 1 (i.e., it is not in the SE). The mental navigation representation of object 3 in OVC at 15.21 seconds looks the same as the mental navigation representation of object 1 at time = 11.36 seconds.
