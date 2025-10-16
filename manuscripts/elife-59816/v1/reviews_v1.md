# Peer review - Round 1

Editors:
- Neil Burgess, University College London United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59816.sa1](https://doi.org/10.7554/eLife.59816.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work identifies a population of neurons in retrosplenial cortex that respond to environmental barriers at a range of distances (weighted towards short distances) some of which are also tuned to the egocentric direction of the barrier. Interestingly, a variety of behavioural, opto- and chemo-genetic manipulations indicate that these are not simple sensory responses, but potentially reflect a representation for egocentric action (such as turning away from barriers) constructed from allocentric representations in the hippocampal formation.

Decision letter after peer review:

Thank you for submitting your article "Entorhinal-retrosplenial circuits for allocentric-egocentric transformation of boundary coding" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Laura Colgin as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation, but do include requests for additional analyses.

Summary:

The authors report e-phys recording of neurons in retrosplenial cortex that respond to environmental barriers (walls, inserted barriers and drop-edges) at a range of distances (weighted towards short distances) and with tuning to the egocentric direction of the barrier (although the amount and distribution of directional tuning is slightly unclear, with 185/485 cells exceeding a >99th percentile in shuffled directionality).

By using darkness, changing the nature of the barrier (walls to drop edges) and cutting whiskers, they show that these responses are not simple unimodal sensory responses. By rotating polarising environmental cues, they show that the tuning of head-direction cells and spatially tuned cells in RSC rotate, but the egocentric directional tuning of the RSC barrier-responding cells is retained.

They compare these to border cells in medial Entorhinal ctx., showing that EC border cells have higher firing rates and can be used to decode the distance to the walls for a longer range (up to 50cm) than RSC cells. The RSC cells with directional tuning are lateralized so that those in one hemisphere tend to be tuned to contralateral egocentric direction (similar to the cells reported by Alexander et al.,). They also show that RSC cells (but not EC border cells) reliably precede upcoming movements (turning away from the barrier).

Finally, they perform chemo- and opto-genetic silencing in each region while recording in the other, showing that the RSC cells are affected by EC input but not vice versa. That is, inactivation of EC by DREADDs reducing tuning and firing rates in RSC, and halorhodopsin or jaws inactivation of EC projections to RSC disrupted RSC cell firing near boundaries, shifting firing to the centre of the environment.

They interpret their results in terms of top-down activation of egocentric responses (turning away from barrier) driven by allocentric representations of barriers in MEC.

The paper is interesting and (mostly) clear, potentially showing a sophisticated egocentric representation generated top-down from allocentric representations. However, there are several issues that would need to be clarified or resolved before publication in eLife.

Essential revisions:

1) Need for much more cautious interpretation of the MEC inactivation experiments. Is it fair to ascribe such a strong role for MEC on the basis of these data, or might it be one of many potential inputs?

a) Subsection “Inhibition of MEC input disrupts border coding in RSC but not vice versa” Figure 5, and associated Supplementary Figures etc. The DREADD experiment shows powerful reduction of affected MEC cells without affecting running speeds. Nice work. The effects on the RSC cells, though, are rather mild. After MEC inactivation, the average EMD boundary template score was 0.186. Yes, this was lower than before inactivation (before was 0.181, p = 0.016), but the net effect of inactivation is that the average EMD-border score is now 0.186 and thus still well under the 99% classification threshold to be defined as a border cell.

b) The ratemap illustrations of this manipulation, Figure 5C left, show two cells, with EMD values before of 0.177 and 0.178 and after of 0.293 and 0.277. Of over 100 border cells, they show the most unrepresentative cell and the third most unrepresentative cell. Something more representative should be shown.

c) Similar points as a) apply to the other two inactivation experiments using optogenetics. The cell-body inhibition results are particularly weak in effect, with laser ON EMD scores averaging 0.0192. This average is 0.001 above the relatively strict 99% threshold of 0.0191, and 0.003 above the second laser off average. Thus, the cells are on average still very border-like.

d) as with b) Similarly unrepresentative cells it seems are shown for Figure 5L and 5N.

e) The disruption of firing caused by inactivation of the MEC seems slight (Figure 5D,O), and the examples in 5L (and to some extent 5N) are not convincing because the firing patterns do not seem stable across the two 'OFF' trials, so it is hard to be sure that changes in the 'ON' trial are due to the manipulation. To what extent does the laser stimulation (Figure 5O) increase the 'messyness' of firing rather than changing its tuning characteristics – eg reducing spatial information/stability or increasing excitability (are firing rates different)?

f) The chemogenetic and optogenetic manipulations are lacking standard controls.

Specifically, there is no non-DREADDs group or sham injection recordings for the chemogenetic experiment, and there is no control virus group in the optogenetic experiments. As such the effect could be due to systemic effects in the former and with heating in the latter. The DREADDs experiments do have an internal control with the RSC-MEC reversal inactivation, but not the optogenetic experiments. That being said, the cell body inhibition experiment gives more confidence in the result.

g) These findings are interpreted with exaggeration.

Abstract "These egocentric representations…require inputs from MEC." Subsection “Inhibition of MEC input disrupts border coding in RSC but not vice versa” "While these DREADDs-mediated manipulation experiments suggest the necessity of MEC signals for border tuning in RSC…". Figure 5 legend: "RSC border cells require input from MEC to maintain their boundary tuning". Necessity and Require are untenable inferences from the modest effects shown, and this should all be rephrased so casual readers are not misled.

They should perform a sanity-check analysis where cells with peak rates of say 1Hz are excluded from the analyses. If a cell is not really firing, it may not be that informative to examine the spatial features of the few available spikes.

h) Subicular boundary related inputs. Boundary coding being both preserved in darkness (Lever et al., 2009; see also Brotons-Mas et al., 2010), and most cells maintaining their tuning without walls present (Lever et al., 2009; Stewart et al., 2014) is shown in the subiculum and thus there is a source of boundary-coding information additional to the Entorhinal cortex that shares some key features with these retrosplenial border cells. The projection to the retrosplenial cortex from the dorsal subiculum, where boundary vector cells have been found, is dense (see e.g. Wyss and Van Groen, 1992). I think Rosene and van Hoesen, 1977 suggest the main cortical afferent to the granular RSC originates in the subiculum. Thus, consideration of boundary information coming into the RSC should mention such boundary cell and anatomy tracing work.

2) What are the defining characteristics of the RSC 'border cells', are they directionally tuned, how do they relate to other boundary-responsive cells, and what to call them?

a) Quantification of border scores is by comparison to a Gaussian smoothed template of firing at the borders. However, the comparison method (earth mover distance, EMD) is not clear – giving an intuitive explanation, such as the total distance moved by all units of firing rate to match the firing rate and template distributions would be helpful. More intuition for the numbers would be gained by showing cells with values near the classification thresholds, not just at/near the tails. Figure 1F shows values of 0.14, 0.145, 0.159…. and then 0.222 and 0.312. Please show cells near 0.1906 cutoff. Relatedly, in Figure 1E, show the EMD values corresponding to 95 and 90% cutoffs.

b) It is not clear the extent to which spiking has to be restricted to the borders of the environment, how the method captures spiking that is displaced a certain distance from a border, and how the distance and egocentric direction tuning of each cell was found. If the template is only at the border are more distally tuned cells missed?

Is this same measure applied to the MEC (for fair comparison of the MEC and RSC it should be)? And does it find cells that fire distant from the border in MEC? This is particularly relevant given the puzzle that spatial representation occurs up to 50cm from the border by MEC 'border cells'? Did distance tuning differ between RSC and MEC (please show the distance tuning distributions for both areas)?

c) The comparison to actual border cells (that must fire continuously along a border) is important – the new score does not penalise gaps in firing (hence the appearance of a grid cell in Figure 5L top left?), nor does it require an allocentric tuning direction (a characteristic of border cells and boundary vector cells).

How strong is the tuning to egocentric direction or are these cells that mostly fire near a border in any direction? 185/485 egocentrically tuned cells seems low. Do 300/485 have no directional modulation, or is there qualitative egocentric modulation but below the statistical threshold? If not directionally modulated at all they can't be classified as either egocentric or allocentric.

The claims made (see also 2d) warrant further investigation of the potential differences between their confirmed egocentric border cells and the potentially numerous allocentric border cells within the RSC. Please provide the distribution of egocentric (and allocentric) directional tuning strengths across the populations of 'border cells' in RSC and MEC.

d) Clarification in the language used in the Abstract, Introduction, and Discussion section seems vital. The authors make much of the distinction between the allocentric boundary cells in other regions, and the egocentric boundary cells here. Furthermore, the abstract offers the summary: 'Border cells in RSC…are sensitive to the animal's direction to nearby borders'. Is Earth Mover Distance (EMD) alone egocentric? If not, and all of the analyses are on the EMD population, the result should not be framed as allocentric to egocentric transformation. If the egocentric border cells were analyzed throughout, that would justify the title and framing.

It is confusing to refer to both the barrier-responsive cells in RSC and the previously documented EC border cells as simply 'border cells', when the two populations appear to be different. 'Border cells' were defined by Solstad et al., 2008 as cells that fire when the animal is right next to a barrier in a specific allocentric direction (thus distinguishing them from the pre-existing 'boundary vector cells'). They subsequently suggested that border cells respond to direct contact with a physically present barrier, unlike 'object vector cells' which also respond to an object suspended above them (Hoydal et al., 2019), or boundary vector cells which can respond to the previous location of a barrier (Poulter et al., bioRxiv). The barrier-responsive RSC cells are clearly not 'border cells' – they can respond to barriers at a distance, some with a tuning to egocentric direction, and (the authors argue) are not a direct sensory response to the barrier.

What should they be called? If they think the population is generally tuned to egocentric direction (this is not clear, see next point below) 'egocentric boundary vector cells' would be technically correct, but is a bit of a mouthful, the main thing to avoid would be calling them something they are not. Perhaps referring to them by a label containing 'RSC' would at least make clear when they are referring to their RSC cells and when they are referring to border cells in EC ('RSC boundary cells' or similar).

e) Description of MEC border cells is a little misleading. "These features are shared with MEC border cells, as their boundary tuning is also maintained without walls present (Solstad et al., 2008)".

The data of Solstad et al., 2008 (Figure S8 and S9) show rather altered firing when walls are removed. (A) Of 10 border cells studied in the wall-no wall manipulation, only one maintained its field in the no wall environment, the others did complex or seemingly rotational remapping. (B) Furthermore, Solstad S9 suggests that the seeming-rotational remapping of border fields occurred despite the directional firing of simultaneously recorded head direction cells' being stable throughout the wall-no wall manipulation. Thus, even the seemingly simple rotational remapping may be more complex. In all, this section thus needs revision and clarification.

3) 'Complete Darkness'. If a darkness condition disrupts, there is less burden on the experimenter to ensure its completeness; e.g. darkness greatly reducing gridness implies vision aids grid cell firing in mice (Chen et al., 2019) is a safe inference, and if the darkness was not complete, this does not matter that much. Here, that the darkness was without effect is the finding itself, so there is a higher burden on the experimenter to detail this manipulation. Details in subsection “Behavioral methods” are minimal. It is valuable to know, e.g.: how the room has been prepared for 'complete darkness' (5 minutes from light to dark is a very fast transition, does this generic intertrial interval apply also to the dark trials?), something of the previous light-exposure background of the rats before each one of the infra-red trials is conducted, what happens in the inter-trial intervals, LED technicalities, including the IR 'bleed' nm range, not just the peak value (850nm?), brightness settings, height of cameras from floor, and so on, enabling replication of the setup. My understanding from Flex3 details on the Optitrack website is that there will be in total over 150 LEDs shining upon the environment from 6 cameras: the phrase 'complete darkness' seems untenable. After adaptation, the rats may be able to see in this. If it really was just 5 minutes between light and dark there is minimal time for adaptation, that will be fine, though the second dark trial may involve some dark adaptation if darkness persists in the inter-trial interval. Also: What were the experimenters doing? E.g. more stationary in the darkness condition than the light condition? For evidence that humans, rats, mice and cats can see in the supposedly invisible infrared spectrum, if they are dark-adapted, see e.g. Pardue et al., 2001 and Palczewskaet al., 2014. A paper on good ferret vision at 870nm may be of interest (Newbold and King, 2009).

4) Object insertion

This manipulation is not yet convincing.

a) Though it features in their abstract as a main finding, there are not many cells for this experiment.

b) It seems sub-optimal that the ROI around the object is square, not circular, and quite a large square.

c) Perhaps 10 cells increase their firing in this large square ROI, and others decrease their firing. A lack of perturbation by object insertion is not self-evident from these data; rather there could be some cell-specificity, with some cells with firing being actively inhibited by the object, and others being excited by it. There seem to be quite large reductions in firing in 3 cells.

d) Thus, their aggregate analysis is perhaps a little simplistic, and misses out cell-specific responses. As there is not much statistical power, it might be simpler just to show the majority of these cell responses in a supplementary figure.

e) Importantly, the EMD templates are biased towards increasing the likelihood of a null finding. Put simply, the walls in the boundary template have two rows of high firing bins near them, whereas in the object template, these same walls have only one row of high firing bins near them, and moreover this row is of lower rate. In marked contrast, the object in the object template has three rows of higher rate bins around it. (To be clear, the authors mention this bias in their Materials and methods section: "adding additional weight in the location of placed objects/walls".) Thus, the object is expected (by the template) to elicit high firing for a more extended distance and at higher rates than that at the boundary even though the boundary is an extended cue and should influence the cell more. There is no need for such a biased hypothesis.

f) More details should be provided as to the previous experience with the objects. Might there be an inhibition by novelty? g) Object size: Figure 2F says the object was 15cm in diameter, but Figure 2—figure supplement 1, part g and the main text says 10cm. Please check and clarify sizes for all experiments, including the size of the ROI around the object.

In summary, there is no doubt whatsoever that the walls exert a greater influence than the object, but that is different from saying that "firing of RSC border cells…is invariant to an object introduced into the maze" (Discussion section). This is not an accurate summary when even their analysis as it stands shows a substantial increase in EMD to the boundary template in the object condition.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Entorhinal-retrosplenial circuits for allocentric-egocentric transformation of boundary coding" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are two remaining issues that need to be addressed before acceptance, as outlined below:

1) The statement in the Abstract where it says the cells "depend on inputs from MEC" should be moderated to something like "are influenced by inputs from MEC" to be more consistent with the point made in the reviews.

2) In the response you say, "we decided to include cells that have minimal firing only in opto/chemogenetic manipulation sessions, as this is a clear indication of disrupted firing due to the manipulation." Please confirm the process by which the population of cells was selected on which to test the effect of the manipulation.
