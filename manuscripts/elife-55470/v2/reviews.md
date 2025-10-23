# Peer review - Round 1

Editors:
- Frances K Skinner, Krembil Research Institute, University Health Network Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55470.sa1](https://doi.org/10.7554/eLife.55470.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Taking advantage of the pyloric network in crustaceans, this computational study beautifully shows how circuits and behaviour can adapt to the effect of temperature changes as a result of smooth adaptations in cellular and channel protein mechanisms, thus preserving the overall function of the circuit.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Temperature compensation in a small rhythmic circuit" as a Research Advance for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after an extensive discussion between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. As you will see, this was not an easy decision, but one in which the reviewers and Reviewing Editor reached consensus.

Summary

We viewed this work as a thorough demonstration of the complex effects of temperature, but the results did not represent enough of a conceptual or mechanistic advance as presented. In essence, although all the authors found the work interesting and visually stunning, several concerns were raised, as detailed below in the reviewers' comments. Further, even though it was felt that the authors could potentially address some of the concerns raised (e.g., re Q10 variation assumptions etc.), all of the reviewers felt that something more besides a descriptive presentation was warranted to justify publication in eLife.

Reviewer #1:

Since the paper that this work is building on is a tools and methods paper, we do not think that it is necessarily appropriate to be considered as a research advance paper, because A) it does not appear to be building on any of the tools and modeling techniques established in their previous publication, and B) it is using those techniques to explore a research topic that was not explored in the original publication. In other words, it would seem to be more appropriate to considered novel research, and not a research advance on the previous tools and methods paper. In their cover letter, the authors also considered this as an option. Our review is considered in the context of a research article.

In this manuscript, the authors use specialized computational methodologies and plotting techniques to uncover how current contributions in a set of models of the pyloric network change with temperature while still robustly generating stereotypical electrophysiological outputs. In selecting the models using their landscape optimization + a screening process approach, they ensured that the models were first capable of robustly generating triphasic spiking in the right order across different temperatures before analyzing current mechanisms through which this output emerges. For these models, they highlight a gradual change in current contributions as temperature is altered, showing that these current changes are complex and do not follow the same trends across models. In essence, they are able to show the existence of multistabilty, hysteresis and in general the non-trivial responses to changes in temperature.

The Marder lab has produced several interesting experimental and modeling studies examining temperature perturbations in previous works and this computational study adds to it. While the modeling work is robustly performed, it was thought that certain aspects of the modeling could be better contextualized in their connections to experimental literature. For example, when looking at hysteresis or removal of certain conductances during temperature changes, do the models – which were not designed to replicate any experimental electrophysiology outputs in these contexts – exhibit changes that are in line with what is seen experimentally (i.e. have there been any comparable experiments performed)? Could the authors consider/describe and/or design experiments that could be performed in light of their findings? For example, the finding that h-currents are not sensitive (and CaT are sensitive) to temperature (Figure 14C). Or perhaps a take-home finding would be that some types of currents (and not others) are sensitive? Is this something that the authors think appropriate in their context?

Reviewer #2:

This study compares models that reproduce operation of the pyloric network across a range of temperatures based on different sets of parameter values. Rather than identifying models that reproduce network operation using different sets of conductance densities (G), they identify models with different sets of G values and Q10 values. They then use their currentscape visualization approach to ascertain that "temperature changes the relative contributions of the current to neuronal activity so that rhythmic activity smoothly slides through changes in mechanisms." Though interesting, there has been a lot of work in this area (i.e. temperature compensation in the pyloric network in particular, and more generally about degeneracy in the STG), which impacts the novelty of the current study. Moreover, I have significant reservations about how Q10 values are treated.

Main Concerns:

1) To my knowledge, the Q10 value for a given process (single channel conductance or gating) in a certain channel type tends to be quite consistent, which means it shouldn't differ much between two individuals of the same species. But if I understand the current study, the Q10 value for a given process is constant across the cells of a given network, but varies between networks. Is that correct? If so, is that justified? This comes up in the Discussion, where a handful of papers about RNA editing are cited. But in Garrett and Rosenthal, 2012, the difference is observed in different (arctic vs tropical) species of octopus. Reenan et al., 2015, address acute temperature effects, but don't report any physiological (Q10) changes. Is there any evidence for this sort of RNA editing in crabs/lobsters? Variation in Q10 values across individual is a critical yet dubious assumption. At the very least, the authors need to be transparent about this at the start of the paper.

2) On the flip side, conductance densities within a network are fixed (i.e. do not vary with temperature). Is that correct? I thought that compensation was mediated via homeostatic changes mediated by changes in ion channel expression (O'Leary and Marder, 2016).

3) There are 37 conductance densities in the model, plus 14 different Q10 values. Even before variations in Q10 values are considered, I suspect that there are many different G values that can produce models that behave appropriately across the full temperature range. Indeed, the solution space is high dimensional, which allows for a variety of solutions. It is not clear to me if the even higher dimensionality afforded by variations in Q10 is really necessary. For instance, if the analysis presented in Figure 4 of this paper (to models with different sets of Q10 and G values) was applied to models with the same Q10 values but different G values, would the results be fundamentally different? Wouldn't the currentscapes still look different because of differences in G values (especially if G values were subject to homeostatic regulation)? I suspect there would still be smooth transitions between different relative fractions of currents. Showing that this doesn't happen without variation in Q10 values is important if a conclusion of this paper is that Q10 variation is critical.

Reviewer #3:

This work uses simulations of a reduced computational model of the crustacean pyloric network to make the important points that (a) neuronal networks that generate multi-phase bursting rhythms may be able to do so robustly across temperature changes despite the fact that these changes have different effects on different currents, and (b) the mechanisms underlying rhythmogenesis, including relative importance of currents, may change with temperature. The work mostly uses methods first presented by the authors in a 2019 eLife paper but looks at new issues.

Given the past works by these authors and others, I do not find these points to be highly surprising, and the paper also has some flaws that I will discuss in more detail below. My general assessment is that the authors' vivid illustration of these points in a computational model is a worthy contribution to the literature, but not a major advance.

Substantive concerns:

1) Much of the paper is written as a show and tell rather than as a flowing narrative. The authors tend to start sentences and paragraphs with phrases like "Figure X shows…" instead of presenting ideas, with figures shown in support of these ideas. I think some significant rewriting is needed to rectify this issue.

2) One of the issues that the authors consider is the relative roles of different currents in rhythms associated with different models and temperatures. I am not sure about the logic here: if a current has a larger magnitude in one regime than another, can we necessarily conclude that it has become more important? It may be that current A has grown larger, but current B has grown larger still; or perhaps current C, which is redundant with A, has also grown larger, such that A is no longer essential for rhythm generation. The authors need to be more careful with how this issue is presented; ideally, they would demonstrate that the changes are not just there, but are also meaningful. In a similar vein, they are making a choice to emphasize features that change between regimes, but there are also features that change very little, and this invariance could be as important as – or more important than – the changes. Finally, the extent of the changes in currents is not quantified – it is just displayed visually across Figures 8-10 and Figure 11. I would like to see some quantification of the changes, and I am not convinced that Figures 8-10 are needed at all since, to me, Figure 11 (which is beautiful) is much more illustrative.

3) I think the Materials and methods section needs some improvements and additions. The authors should clarify how they set up and check their target features for a rhythm to be considered valid – are there specifications for each cell? for the network as a whole? what if activity is rhythmic but not every cell bursts on each cycle? how are temperatures between the 4 main values "surveyed", to ensure that rhythmicity persists? Also, the authors should provide experimental citations for target values used for duty cycles and conductance ranges. I would like some justification for the use of the non-standard reversal potential of -70 mV for glutamate and for why the leak conductance is varied over a much smaller range than other conductances. For those interested in reproducing the results, the authors should indicate what computing resources (desktop? cluster?.…) and coding environment were used and how long simulations took (roughly – are we talking hours, days, weeks?). Finally, how were weights chosen for Equation 6?

4) Although the figures overall are informative and aesthetically pleasing, some revisions and clarifications are needed:

a) Figure 1A: I don't understand the rationale for the phase labels used. Why does the "PD off" box enclose the time when the PD cell is active? Why is there overlap between "LP on" and "LP off"? And so on! Some explanations are needed. Also, I don't see 3 curves in the top panel of Figure 1C, and the "PD, LP, PY" labels are too far removed from the data in the middle panel.

b) Figure 2: Panel B shows 6 examples. It would be nice to have some sort of summary of the findings over many models, not just these 6.

c) Figure 3D: the caption erroneously suggests that the duty cycle is multi-valued in the pink box.

d) Figure 6 and associated text: The authors should indicate how they define "failure" and how they detect it computationally (see (3) above).

e) Figure 11 supplement is lovely but clarification is needed about what p(V) (probability of voltage) means here. I am not seeing any dramatic effects, which makes me wonder if there is any scientific reason to keep this figure.

f) This is a very long paper. I am not convinced that the PCA adds much, and it's especially not clear to me how to get solid information from Figure 12C.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Temperature compensation in a small rhythmic circuit" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gary Westbrook as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Farzan Nadim (Reviewer #2); Alexandre Guet-McCreight (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript uses computational modeling to examine how neural circuits can produce consistent activity across a wide range of temperatures. The authors use a family of models of the crustacean pyloric network, based on prior work from the Marder lab and a recent paper of the same authors. The main finding is that similar activity in the network, at different temperatures, can arise from the dynamic contributions of different currents. Additionally, the study shows that different currents play a compensatory role for one another at different temperatures, and that strong perturbations to the system at different temperatures could result in very different outcomes. It is noteworthy that this detailed level of analysis of current contributions is not possible to do experimentally. Therefore, this work also offers a glimpse at the coordination of ion channel mechanisms that could be occurring beyond the scope of current-day experimental apparatuses.

Essential revisions:

The reviewers found significant improvement over the original version, and the work was found to be comprehensive and worthy. However, concerns still remain. Overall, it was felt that the work as presented was too much on the descriptive side, the current narrative did not reflect what the interesting and important points of the study are. Some insight into why/how the compensation works needs to be provided. Specifics regarding these points are detailed here, and the various minor points raised by the reviewers are given below.

1) The narrative of the results should be changed and arranged around the main points.

That is, the Results narrative should draw the reader's attention to the highlights of the findings and (when allowed) the details should be put in the supplemental figures and tables.

In particular the many details of all the models voltage ranges, duty cycles etc. could be put in figure supplements. For instance, Figure 8, is quite beautiful with its currentscapes, but it is unclear what the point of the figure is? What information is the reader is supposed to take from this? There's no useful information even in the legend. The one point they bring up in the Results is rather subtle (they could've at least put arrows or circles) and the main points they make in the Results are actually in the figure supplements.

2) A problematic point here is that temperature changes are modeled in such an unconstrained manner (with 31 free parameters) that it is difficult to know whether any of the trajectories along different temperatures correspond to real biological changes. Does an ionic current respond to the same temperature change with widely different Q10s across preparations? If every single parameter is variable, independent of the conditions imposed, then what is the point of even measuring it? Would solution trajectories across a range of temperatures show more consistent underpinnings if the Q10s were consistent for each ionic current? In short, I find the unconstrained fitting of the parameters until the right solution is found akin to overfitting a curve to a few data points, and then trying to glean information from that fit. Please speak to this issue in some capacity.

3) There are interesting and important points in the study: 1. compensation of currents for one another at different temperatures (which I presume is a form of homeostasis), 2. Smooth transitions of these currents for one another. 3. Different responses to the same perturbation at different temperatures. 4. Distinct ways that the system crashes at high temperatures and 5. The presence of temperature-dependent hysteresis. However, the narrative in the presentation of the results (especially in the first half) is mainly descriptive and detail oriented, rather than driven by questions.

4) If one point of the study is that getting similar solutions at different temperatures requires ionic currents to assume different levels of contribution, this could be set as a central question and shown more directly. What is learned from how the models "crash" at high temperature? There may be some lessons there, but this point is not properly analyzed or explored.

Similarly, with the hysteresis. What is the lesson and what does it have to do with temperature or temperature compensation, rather than simply that a set of parameters may result in multistability?

5) Subsection “Spiking patterns during temperature ramps” and Figure 3E: Although clearer in this updated manuscript, can the authors add something to the figure to make this more obvious (e.g. adding the number of spikes in each burst above each burst in the trace or adding an inset plot showing superimposed traces of a cycle with and a cycle without the extra spike). Without actually counting the number of spikes in each cycle it's not obvious to me just from looking at the trace.

6) Paragraph three subsection “Spiking patterns during temperature ramps”: If these spiking patterns can be compared to experimental recordings, why is it the case that they are not compared here? In fact, this paragraph appears to end abruptly without much dissemination of Figure 4. I'm also hesitant on calling the duty cycle "temperature invariant", since it seems clear from Figure 4 that duty cycle definitely does vary with temperature to some degree – how the authors seem to define temperature-invariant strikes me as a bit too qualitative.

7) Paragraph six of subsection “Dynamics of the currents at different temperatures”: There are a lot of qualitative observations made regarding changes in currents across temperature and models. I feel as though this is an easy trap to fall into when there are many qualitative observations that could be made – for the reader, I find it becomes hard to follow since I end up going through the figures and squinting to try and see exactly what point the authors are trying to make for each observation. The main point is stated at the end and is very simple and much less specific: "Together, these examples illustrate how a current can play different roles at different temperatures, and how diverse these mechanisms can be across individual solutions". To bring this point forward better, I suggest the authors cut down on specific qualitative observations that individually do not carry much weight and speak more broadly. For example, you could replace the third sentence with something like "the current contributions profiles in model 2 are different leading up to and following bursts". Though I highlight this paragraph, I also feel that the writing is like this at various other points in the results as well.

8) Final paragraph of subsection “Dynamics of the currents at different temperatures”: Is there a case where current contribution transitions across temperature are not smooth? And is there any reason to believe that they would not be smooth in the first place? If not, I would argue that this does not seem like a very surprising finding given that many e-phys features are preserved and change gradually with temperature themselves. Of course, it is still informative as to why the e-phys features change gradually – just not really surprising. Perhaps some of the points put forth in the discussion should be first mentioned at this stage in the results to help the reader better understand why this finding is both important and non-intuitive.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Temperature compensation in a small rhythmic circuit" for consideration by eLife. Your revised article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Gary Westbrook as the Senior Editor The following individuals involved in review of your submission have agreed to reveal their identity: Farzan Nadim (Reviewer #2); Alexandre Guet-McCreight (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus, the revisions requested below only address clarity and presentation.

Summary:

This manuscript uses computational modeling to examine how neural circuits can produce consistent activity across a wide range of temperatures. The authors use a family of models of the crustacean pyloric network, based on prior work from the Marder lab and a recent paper of the same authors. The main finding is that similar activity in the network, at different temperatures, can arise from the dynamic contributions of different currents. Additionally, the study shows that different currents play a compensatory role for one another at different temperatures, and that strong perturbations to the system at different temperatures could result in very different outcomes.

Essential revisions:

All the reviewers found that the work was improved with better flow and was less descriptive. There are two aspects that the reviewers think should be addressed

1) Although the hysteresis result is very interesting, the motivation for looking at it in the context of temperature sensitivity/robustness still isn't provided, nor is the biological link. This aspect of the paper would benefit from providing more biological context about the significance of multistability with respect to temperature sensitivity.

2) Clarification of the authors' treatment of Q10s with a reasonable justification in the discussion, rather than hand waving. Specifically, although it is safe to assume that not all of the Q10 values are known and the authors set reasonable bounds when fitting the Q10 values, the concern is not that the Q10 for membrane current X sits somewhere between 1 and 4, but that the Q10 for membrane current X differs between models A, B and C when, in fact, the molecular identify of current X is the same in all of those models, because a Q10 value is not something that is regulated. Thus, if the authors took the set of Q10 values from model A or B or C, and then, using that set of fixed Q10 values, re-ran their genetic algorithm to determine new sets of conductance combinations that produce an acceptable triphasic rhythm, one might expect that successful conductance combinations will be far less diverse than when Q10 values are allowed to differ (as shown in Figure 1—figure supplement 1B). Without knowing the real Q10 values, we still won't know what the real conductance combinations could be, but we'd have a clearer picture of how diverse those combinations could be under biologically realistic conditions.

Although we encourage such additional simulations, it is not a requirement. However, an expanded discussion of how Q10's are treated is warranted.
