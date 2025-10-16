# Peer review - Round 1

Editors:
- Julie PI Welburn, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91719.sa0](https://doi.org/10.7554/eLife.91719.sa0)

This paper represents an important study for the microtubule cytoskeleton research community. By employing computational simulation, cell-free biophysical assays, and live-cell imaging, Gonzalez et al. convincingly reveal a mechanistic insight into the EB1 tip-tracking activity at the growing microtubule plus ends, preferential binding of GTP- over GDP-microtubule protofilaments does not fully explain the plus tip tracking of EB1. The authors show a binding preference of EB1 for protofilament edges over the closed lattice, which together with the nucleotide-state dependent dissociation rate of EB1 from the closed lattice successfully recapitulates the efficiency of EB1 tip tracking.


---

# Peer review - Round 1

Editors:
- Julie PI Welburn, https://ror.org/01nrxwf90 University of Edinburgh United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91719.sa1](https://doi.org/10.7554/eLife.91719.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Rapid binding to protofilament edge sites facilitates tip tracking of EB1 at growing microtubule plus-ends" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife.

Our decision reflects the content of individual reviews and the outcome of the consultation session. All reviewers and the editor thought that the study was potentially important and could change the way how we think about the mechanism underlying the accumulation of End Binding (EB) proteins at growing microtubule plus ends, a topic of considerable interest to the cytoskeletal community. However, significant concerns were raised both about the experimental and computational aspects of the study. Given that this is the second manuscript developing the idea of EB proteins binding to protofilaments edges, compelling experimental evidence supporting the conclusions would be needed to make this study suitable for eLife.

1. Concerns about the experimental part. The conclusions strongly rely on the use of Eribulin, which the authors propose to bind to protofilament edges and directly interfere with EB binding to protofilament edges. The evidence for this is insufficiently compelling. First, contrary to what the authors claim (but do not illustrate anywhere in the manuscript), there seems to be no steric overlap between the binding sites of Eribulin (which binds to the longitudinal interface of β-tubulin) and EB CH domain (which binds predominantly to the lateral tubulin interfaces, see attached figure). The EM data included in the manuscript confirm the fluorescence microscopy data, previously published by Doodhi et al., that Eribulin binds to microtubule ends and not to shafts. These EM data do not have sufficient resolution to pinpoint the exact binding site. Another problem is that the effect of Eribulin on EB comets can be explained in different ways. Low concentrations of Eribulin, as well as most other microtubule-depolymerizing agents, indeed have limited effects on microtubule growth rates but trigger catastrophes, presumably by affecting microtubule tip structure. Changes in microtubule tip structure can affect EB binding. Therefore, a comparison of the effects of different concentrations of different compounds, with and without steric overlap with the EB binding site, could be a useful approach. For example, Halichondrin could be a drug candidate with a binding site strongly overlapping with that of EB.

2. Concerns about the computational part. While the simulations currently represent the strongest part of the manuscript, there were also some significant criticisms, as outlined in the individual reviews. In particular, the reviewers had questions about the sensitivity of the model output to the parameter values. They also thought that it would be important to prove that the simulations reproduce microtubule dynamics, including catastrophe frequencies, successfully, and consider alternative models of microtubule tip structure (with flared, rather than tapered protofilaments – a model that is gaining popularity in the field). The potential difference in the accumulation of EB monomers vs dimers also needs to be discussed.

Since addressing these concerns would require very significant efforts and their outcome appears uncertain at the moment, we return the paper to you. However, if you think that you can address all these concerns in full, we will be happy to reconsider this manuscript. It will then be treated as a new submission, but we will do our best to send it to the same reviewers. If you decide to resubmit to eLife, please provide a point-by-point rebuttal to all comments.

Reviewer #1 (Recommendations for the authors):

Gonzalez et al. have studied the molecular mechanism of end-tracking by EB proteins. In 2019, the Gardner lab published a study of end-tracking that used Brownian dynamics simulations to argue that EB binds more rapidly to "protofilament edge sites" (Reid et al. eLife 2019). Those simulations used static lattice structures and simulated the diffusion of EB into these edge sites. The present manuscript extends this line of inquiry with a simulation of dynamic microtubules that implements an accelerated rate of binding to protofilament edge sites. They show that the simulation matches experimental data for end-tracking, particularly with regard to the gap between the microtubule tip and the EB comet position (Figure 1C).

My first comment concerns the sensitivity of the model output to the parameter values. The authors write: "Even the most sensitive parameters had at least an 8-fold range of acceptable values", with the data shown in Figure S1. But I'm confused as to how this relates to Figure 2E and 2F, where end-tracking is lost when the edge-binding parameter is turned off. The lack of sensitivity that the authors state early in the manuscript seems in conflict with a lot of the rest of the paper, where they adjust parameters and show that the model breaks. Perhaps it's because I'm having difficulty relating the actual parameter values used in the model with the ranges used in Figure S1, for example. However, elsewhere in the paper, they say "the simulation predicts that reducing the protofilament-edge on-rate by 4-fold will lead to a dramatic loss of Mal3-GFP intensity at the tips of dynamic microtubules". So: does a 4-fold change in a parameter kill the model or is there an 8-fold range at which everything is fine? The authors need to clarify which parameters of the model are important.

My second comment about the model is that there is no validation that it reproduces microtubule dynamics successfully, although the simulation is well established in the Gardner lab so I'm sure they have considered these issues. But importantly: does the simulation accurately reproduce catastrophes? Presumably, the catastrophe frequency is related to the hydrolysis rate constant, and the hydrolysis rate constant will determine the relative size of the GTP-cap. Presumably, the size of the GTP cap is significant for the model's performance, especially for the relative significance of the closed-lattice on-rate vs. edge on-rate. If I understand correctly, if there is a larger GTP zone, then a higher on-rate to the closed lattice will shift the EB signal further away from the microtubule end.

The simulation is validated by a few different types of experimental data, most notably experiments using Eribulin. The authors use a relatively low concentration of Eribulin, which does not reduce the microtubule growth rate, but which does, in their hands, cause a modest reduction in Mal3 end "tip specificity" (Figure 4C and Figure 5B). This data, while promising, is a relatively weak anchor point for their computational work at this time. Only one Eribulin concentration is used in each experiment (80 nM for the in vitro work, 50 nM for the work in cells). In comparison, Doodhi et al. went as high as 250 nM Eribulin. At these high concentrations, the microtubule growth rate starts to decrease, but presumably, this effect can also be understood within the context of their computational framework. If they observed a dose-dependence of the Eribulin response, their argument would be strengthened.

The authors claim that Eribulin blocks the EB site at protofilament edges. This point would be much clearer to the reader if the authors created a structured figure panel for their paper, e.g., one that highlights the residues that interact with Eribulin alongside the residues that interact with EB.

Lastly, the paper assumes a structure for the microtubule end that is consistent with the lab's previous work and with many people's ideas in the field, namely that the end is tapered. It's worth noting, however, that the structure of the end is not a settled manner, with the McIntosh lab and their collaborators taking a decidedly different view of the end. While McIntosh's flared growing ends would have lots of edge sites, it's the lack of a taper that prevents a problem. Without some protofilaments being longer than others, the EB signal will not be displaced back from the end of the microtubule in the same way. The paper needs to address this issue for the reader so that a less-experienced reader (e.g., an early graduate student) will not have a false sense of a settled issue. Could a McIntosh model for the microtubule end make sense in terms of EB end-tracking as these authors understand it?

The raw data on the EM is very close-cropped (Figure 3B), so it's hard to see if the gold particles are consistently edge-bound or if the examples are just a lucky few where the gold particle happened to be near the side.

The Introduction includes a "reference dump", in which a single sentence is followed by a large number of references (in this case, 12). I sympathize with the desire to cite all of our colleagues, but I consider such reference dumps to be suboptimal because the reader does not really know why each paper is being cited.

Reviewer #2 (Recommendations for the authors):

This manuscript aims to explore and understand the mechanisms by which EB1-family proteins achieve their characteristic pattern of end-recognition. The work rests heavily on kinetic simulations but also incorporates experimental data to support assumptions and/or validate predictions. I found the work to be interesting. I think it is most convincing in its demonstration that differences in binding to 'complete' GTP- vs GDP-lattice sites cannot recapitulate observed aspects of EB comets – some end-specific recognition features are required. The authors postulate a particular kind of end-specific feature ('edge sites'), but it seems others might be possible. Some moderation in language and/or more explicit acknowledgment that other end-specific features may be operating might be helpful in this regard (and would not detract from the interest of the work).

The use of kinetic simulations is a strength of the work because it allows the authors to directly test different assumptions, and explore alternative models. The computational work is generally well-done, and it was particularly helpful to see results across a range of parameter values. The conclusion that distinguishing between 'closed' GTP- and GDP- lattice sites is not sufficient to recapitulate plus-end tracking is also interesting and considered a strength. The main weakness concerns whether the Eribulin data can be interpreted in the way the authors state. Additional weaknesses include a too-brief description of the modeling in the main text and too little quantitative engagement with prior work on EB comets.

The authors state that Eribulin can interfere with the EB binding site. My understanding from the Doodhi et al. paper cited is that Eribulin binds the plus-end of ab-tubulin and when bound at the end of a protofilament effectively blocks its elongation. I think at the very least the authors should add a figure panel to show a model of the eribulin and EB binding sites, to put things into structural context and provide better support for the statements that eribulin can bind to protofilament edge sites. An alternative view might be that Eribulin is doing something to change the shape of the microtubule end or the conformation of tubulin near the microtubule end, and these latter changes are influencing EB binding. Because the eribulin data provide the main experimental support for the claims that emerge from the model, this is an important aspect of the manuscript that needs some shoring up.

The essence of the underlying polymerization model is described in one sentence in the main text ("The tubulin assembly portion …"). This is too brief. The authors should expand the description somewhat to make the models and their assumptions more obvious for someone not interested in jumping to the methods section. It would also be nice to have some cartoons illustrating what sorts of end structures their simulations are generating (how tapered are they and is there detectable protofilament splaying), and how the model parameters relate to other models such as those previously used in the Gardner lab. For example, koff(GTP)/kon = 16 nM if I calculated correctly – does that correspond to a longitudinal interaction? If so, the affinity is rather strong relative to other models in the literature.

Finally, it would be helpful for the authors to more explicitly interpret their explicit simulations in light of simpler models like those proposed in the Maurer et al. work from the Surrey group, in which a relatively simple kinetic scheme could recapitulate observed features of EB comets. Can the authors make some more or less quantitative comparison between their results and these prior simpler schemes, both in terms of the basic reactions but also the quantitative parameters used in each model (association rates, for example)? Doing so would round out the manuscript and make it more appealing.

Overall I found the manuscript to be interesting – while on one hand, it might seem obvious to state that some end-specific binding feature is important for the end-localization of EB, much of the structural explanation for EB has focused on differences between GTP and GDP lattices, which the authors show is not sufficient.

I have two additional questions.

First – would the authors consider softening or doing more explaining around 'protofilament edge sites' and what that might encompass? It's a very specific phrase and made me wonder whether other end-specific features (partial curvature, say) might also suffice to give good-looking EB-localization in simulations. Basically, the authors are postulating an awfully specific mechanism given the supporting experimental data. So, I think it would be good to discuss this more, possibly raising (or even ruling out) alternatives. Do they think their results are general in the sense that they might also apply to CAMSAP proteins at the minus end?

Second – if EB associates more slowly to 'closed' sites on the lattice, should tubulin associate more slowly to EB-occupied 'edge sites', or are those closing events mainly happening by the kind of 'isomerization' reaction mimicking protofilament:protofilament pairing? These might be useful issues to add to a more fleshed-out description of the model and what it does and does not encompass.

The authors might also consider making their summary figure (currently 5F) a new standalone. I thought its impact was diminished by being combined with cellular data.

Reviewer #3 (Recommendations for the authors):

The authors investigate the mechanism by which tip tracking proteins EB recognize and bind microtubule tips. Earlier simulations from this group suggest that EB binds much faster at the edge of the microtubule where the lattice is not yet fully formed because reduced steric hindrance allows faster and easier landing of diffusing EBs on microtubule binding sites. Authors propose that if this acceleration in binding is more significant than the acceleration of detachment from these sites (which would also always happen because the site is not complete), the overall recruitment to the edge is more efficient than the recruitment to the closed GTP lattice itself.

Thus, the authors propose that in growing microtubules binding of EB occurs predominantly at the edge. As the microtubule elongates, these EB molecules get incorporated into the lattice of the GTP cap and detach when the lattice changes from GTP to GDP.

To test this idea, the authors use clever experiments. First, they show that the drug Eribulin recognizes incomplete (edge) EB binding sites and competes with EB for binding. Moderate concentrations of Eribulin do not reduce the microtubule growth rate but do reduce the relative number of EBs on the tips. This suggests that at least partially binding to the edge does facilitate EB loading to the microtubule tips. Authors take this a step further and argue that it is in fact always the edge where EBs bind and binding directly to the GTP cap does not play any significant role. To show this, the authors use simulations. They find that at a specific set of parameters binding of EBs at the edge can reproduce observed microscopic distributions of EBs on microtubule tips and predict that their experiments are fully explained by EB binding to the edge only.

I find experiments quite solid. I also find that the model needs improvement before it can explain events at the microtubule tips as it doesn't explain some of the most fundamental EB tip tracking properties. Therefore, using the simulations to prove that it is only the edge of the microtubule where EBs bind doesn't seem too convincing. Here are more detailed comments:

1. Simulations have many parameters. It is important to understand which parameters are estimated from experimental data and which are variables. Uncertainties in parameters and which parameters are more important and which are less should be better explained. For example, the ability of EB to bind better to the edge, critical for the conclusions of the paper, is the result of two rates. The on-rate, which is increased ~ 70 times, and the off-rate, which is increased ~10 times. Where did the latter number come from and what is the associated uncertainty? If it was close to 70, there would be no overall difference between the binding to the edge or binding directly to the cap. It should also be clarified for the rate related to the closed-lattice.

2. The model presented in the text and summarized in Figure 5F proposes how monomers of EB can track microtubule tips. However, there is a number of very convincing studies showing that monomers in fact cannot track microtubule tips. EB has to be a dimer to be able to recognize and track the tip. For example, if you dissociate dimers in real-time, they can no longer track microtubule tips (https://doi.org/10.1038/s41556-017-0028-5). It is confusing that authors first find parameters that would allow monomers to tip track and validate their simulations made for monomers using the experimental data, which should represent the behaviour of dimers. It makes validation arguably difficult. Before the model can be used to make predictions about where exactly EBs bind, it should be able to explain why EB monomers do not track microtubule tips and how EB dimers do. This seems like a big difference, so it is difficult to see if or how this more realistic model would lead to the same interpretation of the experimental data.

3. The simulations that show that just the edge binding alone is sufficient to account for the profiles of microtubules observed in microscopy experiments need to be better explained. We do know that GTP caps can be long (e.g. https://doi.org/10.7554/eLife.51992) and in growing microtubules, there should be a lot more EBs sitting on the GTP lattice as compared to the number of EBs sitting on the edge simply because there are more closed-lattice sites regardless of how EB ends up there. Therefore, the shape of the experimental profile should have a much stronger contribution from the EBs sitting on the closed lattice as opposed to those sitting on the edge. If this is true, why would simulations explain the data only assuming zero closed-lattice binding and not direct binding to the GTP cap? What about the opposite experiments? It is very likely, that one could find a set of closed-lattice off-rates that would explain experimental data by assuming only direct binding to the closed lattice and no binding to the edge whatsoever. Can these explain the experimental results?

4. One prediction from only edge binding may be that microtubules growing in the presence of GTPgS should have very specific EB comets. Since incorporation at the edge is expected to be the same, the brightness at the tips should be the same as for GTP microtubules, but the comet should be significantly longer and tail off at a specific distance as the closed-lattice off rate should remain that of GTP. However, if it is only closed-lattice binding there should be no specific comet seen on GTPgS microtubules. Maybe the EB profile in these experiments can be used to extract exactly how much binding can be attributed to the lattice and how much to the edge?

5. In growing microtubules majority of EBs are expected to be at the closed-lattice of the GTP cap simply because the number of these sites should be higher than the number of the edge sites. Let's say it is 10%, 50%, or 100% of EBs that sit on the closed-lattice are incorporated by the edge binding and the rest by direct GTP closed-lattice binding. Would that have an impact on the regulation of microtubule dynamic instability of other tip interactions? Are there any other potential implications?

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Rapid binding to protofilament edge sites facilitates tip tracking of EB1 at growing microtubule plus-ends" for further consideration by eLife. Your revised article has been evaluated by Amy Andreotti (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

1) Provide a detailed analysis/simulation of the split Mal3 comets

Reviewer #3 (Recommendations for the authors):

Gonzalez et al. employ an interdisciplinary approach to dissecting the molecular mechanism by which EB1 tracks the growing microtubule plus ends. In particular, the authors propose that the rapid binding to a special feature, the 'protofilament edge' and the differential binding affinity for the close lattice in GTP or GDP state facilitates efficient tip tracking activity of EB1 at growing microtubule ends. Solid experiment data support the computational simulation. As the authors have thoroughly addressed the reviewers' questions, I only have a few comments that might further improve the clarity.

1. A more detailed analysis/simulation of the split Mal3 comets

The split EB1 comets (Figure 3) are a good opportunity to test the 'protofilament edge-binding' model. The authors quantify the summed intensity of Mal3 and show an ~80% increase in the split comets, supporting additional protofilament-edge binding sites at the growing microtubules with split comets. However, as the split comets are usually quite well separated, it is counterintuitive that the continuously exposed 'protofilament edge' can cause the split comets. Is it possible to simulate the split comets? Also, it appears that the split comet in Figure 3A tracks the depolymerizing microtubules. Is it common? What is the possible explanation?

2. The mechanism by which EB1 peak is behind the very tip of microtubules.

As EB1 binds to the protofilament edge with a 5~7-fold higher affinity than to the close lattice, the location of the EB1 peak seems dependent on the protofilament density (either tapered or flared). Have the authors examined the EB1 tip tracking on microtubules with different end structures? For example, how would the EB1 comet look on microtubules with blunt but flared ends?

3. When I read the manuscript, I wondered how this current model could improve our understanding of the EB1 tip-tracking activity in the context of the model proposed by Maurer et al. 2014. From my point of view, the major conceptual advance is that the rapid binding to the 'protofilament edge' can explain the behaviors of EB1 at the growing microtubule ends without introducing an 'exclusion zone' as proposed in Maurer's model. The authors should compare Maurer's model earlier in the manuscript rather than later in the discussion.
