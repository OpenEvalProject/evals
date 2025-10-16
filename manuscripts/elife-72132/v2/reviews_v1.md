# Peer review - Round 1

Editors:
- Kirsten HWJ ten Tusscher, IBB, Department of Biology, Faculty of Science, Utrecht University Utrecht Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72132.sa0](https://doi.org/10.7554/eLife.72132.sa0)

The authors have created the first detailed model combining the mechanics of root growth with the dynamic regulation of auxin transport and patterning. Their novel model is capable of explaining the anisotropic longitudinal growth of plant roots and the complicated patterns of polarized auxin transport underlying auxin patterning.


---

# Peer review - Round 1

Editors:
- Kirsten HWJ ten Tusscher, IBB, Department of Biology, Faculty of Science, Utrecht University Utrecht Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72132.sa1](https://doi.org/10.7554/eLife.72132.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "A coupled mechano-biochemical framework for root meristem morphogenesis" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Detlef Weigel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Victoria Mironova (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

While all 3 reviewers highly value the novel biochemical-mechanical modeling framework developed and its use for studying plant root development and beyond, they all 3 raised major concerns regarding the claims that are made, the biological correctness of some of the model assumptions, and the clarity and transparancy with which modeling assumptions and limitations are being discussed.

Essential revisions:

1) The authors are required to more extensively discuss modeling details, assumptions and limitations. PDB methodology, how cytoskeleton and how PIN polarisation are modeled should get more attention in the main text. Also, the PIN patterning that is claimed to arise in a self-organized manner is clearly driven by the imposed auxin sources and sinks. Similarly, growth anisotropy derives from the growth asymmetry imposed, so it is not self-organized but has a clear directional source of information. This matters should be discussed explicitly.

2) In line with the above, the authors should tone down their conclusions regarding the self-organized nature of the patterning they observe, and make explicit what inputs are needed to get the patterning they observe. This requires adjustment of the title.

3) The authors should carefully check the biological correctness of the assumptions. As one reviewer pointed out the assumed relationships between microtubules, trafficking and PIN polarity are incorrect.

Reviewer #1 (Recommendations for the authors):

1. line 47 on first mention of growth anisotropy it should be explained what exactly is meant for readers not familiar with the subject.

2. Lines 67-70: The authors couple symmetry breaking and anisotropic growth with polar auxin transport. It should be clarified to what extent the experimental evidence supports this coupling and to what extent it is an assumption.

3. Line 97 a bit more explanation of what PBD does would be nice, remains rather vague/abstract here. i.e. what do the constraints do, is there some Hamiltonian incorporating these constraints that should be minimized? Something else?

4. It should be clarified whether simulations shown in Figure 1A and B contain auxin dynamics (I suppose not?) or only include tissue mechanics. Also, the authors should adjust the depiction of CMT orientation, even at 400% zoom the arrows drawn now are unfortunately hardly visible. Finally, here and for all later simulations it should be clarified in the legend for how long simulations were run.

5. Figure 1D: on the y-axis it states "growth increase per hour", what exactly is meant here

a growth rate increase, or a size increase? Please clarify.

6. CTM should read CMT at line 138/146/150?

7. Presumably at some point also the hypocotyl growth speed will increase. Is the model capable of sustaining root growth anisotropy if after an initial period of growth rate differences between radicle and adjoining tissue the adjoining tissue starts to grow at a similar speed? How does this depend on auxin dynamics?

8. Around line 145 a short mention of the relevance of intramembrane PIN diffusion and PIN internalization would be in place; anisotropic delivery of proteins only results in anisotropic patterns if diffusion is limited and/or proteins are continuously internalized and redeposited, a matter on which the last author has previously done excellent work.

9. Starting at lines 154 the authors compare two methods for auxin-driven PIN polarization. However, the second method, the so-called regulator polarizer mechanism, functions essentially the same as the first, the with-the-flux method, in that both promote PIN deposition at the location of highest auxin flux. The authors should explain why they compare these two PIN polarization mechanisms, what are their essential differences (i.e. why do the mechanisms give different results predominantly for lateral PIN orientations) , and why they did not investigate another frequently investigated PIN polarization mechanism generally referred to as up-the-gradient polarization. The way it is presented now is confusing, as less technical readers may get the wrong impression that it is with the flux and up the gradient type mechanisms that are compared.

Secondly, as the authors state, the regulator-polarizer mechanism is essentially a Turing-type reaction diffusion patterning mechanism within the cell, which typically have a characteristic parameter dependent wavelength. How does such a characteristic wavelength impact the potential of this mechanism to correctly polarize cells of different sizes as occur in the modeled root tip?

10. The authors state they implement an apolar AUX/LAX pattern for cells, however it is unclear whether this pattern is applied for all cells or only for particular cell types, as has often been the case in other studies. Please clarify.

11. Also, in light of different modeling approaches in the field, the authors should clarify in their main text if their model allows for a single intracellular and intrawall auxin concentration or rather allows for intracellular and intrawall concentration gradients. Additionally they should clarify in the main text whether it is intra or extracellular auxin concentrations governing cell growth. Finally, if it is a single intracellular auxin concentration that governs growth, does this not imply that auxin and PIN patterning merely impact growth rate of cells and not growth anisotropy? Please clarify.

12. The article claims to explain the self-organized growth and patterning of the plant root tip. However in the model the authors impose an auxin source in the middle vascular files and an auxin sink in the topmost outer cell files, thus quite a bit of auxin-related prepatterning is superimposed. Indeed, in a sense the polarity of auxin transport outside the modeled root tip domain was superimposed and the modeled domain should merely align accordingly, rather then truly self-organize its PIN patterning. The authors should adress this issue more explicitly.

The authors could test whether imposing either only vascular influx or top epidermal sinks or only a transient signal would suffice to induce correct PIN patterning (I presume that in Figure 3 the auxin source is only removed after the PIN pattern was established, not from the beginning onwards) ? Even more important, the authors should test to what extent mechanical feedback is necessary for the observed PIN patterning given the imposed auxin source and sink locations and auxin-PIN feedback mechanisms (of course in these simulations PIN membrane delivery should be made independent from CMT orientation). Finally, in cells with lateral inwards PIN, is CMT organization also less longitudinally and more diagonally or even transversally oriented, and if so how does this arise from tissue growth mechanics? Please clarify.

13. line 206, please specify which type/subset of parameters could be fitted based on these data.

14. line 210, please specify the nature of the peak (i.e. a peak of what).

15. For Figure 2H-K please clarify whether the shown 1D profiles are for a specific cell file, or rather an average across all cell files for that particular position along the longitudinal axis.

16. Line 214 please consider reformulating "eventually reproducing the non-trivial shape of the root". The model reproduces growth direction anisotropy and PIN and auxin patterning, yet as far as I can judge does not provide an explanation for the wedge shape of the root tip, or the precise organization of the SCN and the differentially oriented divisions occurring there or the precise number of cell files present in the root tip.

17. Line 238 Please clarify the "plausible range of parameter values" statement. Over what range were parameters varied, which parameters?

18. Line 239 please consider reformulating "prediction" into "emergent property", as the phenomenon has long been known it can hardly be seen as a model prediction, at the same time that it automatically arises from the model as an emergent property does deserve more attention.

Also, the authors could possibly test the explanation they offer for the bidirectional auxin flow in the cortex by artificially manipulating epidermis/lateral root cap auxin flow and seeing how this affects cortical PIN patterning.

19. In Figure 3C it appears as if -compared to Figure 3D- PIN proteins are not or hardly present on the membrane. Please clarify and explicitly discuss this matter in the text.

20. Auxin levels in Figure 2C/E-G and Figure 5A in particularly the vasculature seem much lower than in Figure 3C/D. Please clarify?

21. In Figure 3E and F, where in the root are growth rate or auxin concentration measured. Please clarify in figure legend.

22. Figure 5D, the cartoon to the left suggests that in the root tip cut experiment only downward PIN mediated auxin flow occurs, please clarify if this is an emergent result from the root tip cut or rather that PIN2 mediated flow has been abolished.

23. Figure 5E, please clarify whether the narrowness of the root at the top is a result of imposed mechanical boundary conditions.

24. Line 354 Please replace predict with reproduce.

25. In the discussion the authors should be a bit more modest in their statements on the models ability to reassemble key root properties given the importance of superimposed mechanical asymmetries, auxin sources and sinks as discussed earlier.

26. The authors should describe in the main text in a bit more detail how exactly does auxin translate into cellular growth rate and how does this ensure stable, coordinated growth across cell files. In a previous study it was shown that since auxin levels differ significantly across cell files (e.g. much higher in vasculature than in neighboring cell files), problems in coordinated cell growth may occur (https://pubmed.ncbi.nlm.nih.gov/25358093/). Why is that not happening here. Please explain.

27. In the discussion authors mention possible uses of the model such as studying tropisms. However the latter requires incorporating an elongation zone in which cells undergo rapid and extreme cell elongation. It seems that the current model only incorporates slow cytoplasmic cell growth and division occurring in the meristem, would the used model formalism be capable of describing rapid cell elongation? Would the model formalism be capable of simulating the growth asymmetries occurring in root tropisms?

28. The simulation code is made available to reviewers, Will the code be made publicly available upon publication?

29. Equation 4 and descriptions thereof: would it not make more sense to denote this as apoplastic rather than membrane auxin levels (although I realize apoplast and membrane are a single entity in the model formalism). Also the subscript in the first term should not read cell i but membrane/apoplast i I believe.

30. Equation 7, the authors state that auxin decay rate increases beyond a certain threshold auxin level, they should add on what experimental data this is based.

31. Equations 8 and 9: what do the terms AUX1_cell*AUX1_tr and PIN_cell*PIN_tr mean? Only later clear it is about trafficking, explain at first occurrence please.

32. The model contains quite a lot of non-linear interactions, with particularly for the flux and regulator-polarizer model powers of 4, the authors should clarify if model outcomes critically depend on these strong non-linearities.

General comment: English grammar is quite poor, requires correction.

Reviewer #2 (Recommendations for the authors):

Some points would require attention:

1) Misconception on the role of cytoplasmic microtubules: "CTMs restrict the deposition of various protein cargoes on the plasma membrane, typically along the maximal growth direction (maximal strain) (Adamowski et al., 2019; Nieuwland et al., 2016; Siegrist and Doe, 2007; Yang, 2008). It is plausible that PIN protein allocation (and/or other cargoes) at the plasma membrane might be restricted by CTMs." I have a problem with this claim. In Heisler 2010, it was shown that PIN1 remains polarly localized when microtubules are depolymerized. How does that fit with this model? Wouldn't it make more sense to involve the link between CESA and PIN1 (Feraru), or membrane tension and vesicle trafficking (Nakayama 2012, Heisler 2010)? I think the authors rather want to say that mechanical stress is vectorial in essence, and thus could guide both growth anisotropy and growth direction. However:

(i) at cellular scale, it is difficult to envision a mechanism that would be sensitive enough to respond to small differences in stress (this was assumed in Heisler 2010, but it remains a weak point of that study). This is however well described in animal system (membrane tension promotes exocytosis and inhibits endocytosis, see Asnacios and Hamant 2012).

(ii) mechanical stress would not explain the initial differences in growth rates in any case.

I thus agree with the authors that polarity must involve extra cues of biochemical nature, possibly working in synergy with stress. But the rationale should be better explained. In particular, in the model description "CMTs and auxin flux/concentration are the main contributors to PINs localization" is unlikely to be true since PIN localization primarily depends on actin filaments (see e.g. Geldner 2001). Rather, CMTs, as proxy of stress direction, match PIN localization. I believe that the authors would be better off with a model in which instead of cytoplasmic microtubules, actin filaments are modeled (i.e. the MFcell vector). This would not change much in terms of simulations, but it would be more accurate (actin filaments are also believed to align with tensile stress, see e.g. Goodbody and Lloyd 1990).

2) Symmetry breaking event: The idea that the radicle behaves like a trichome in sepals (in Hervieux 2017) is appealing. Maybe I would make the comparison with trichomes more obvious, because it is probably easier to grasp the idea in the case of the trichome (i.e. that a fast growing zone generates mechanical shielding (circumferential CMTs in adjacent cells) and thus anisotropic growth of the radicle). However, figure 1A,B only shows simulation, and figure 1 does not show CMT orientation. So the wording should be checked. For instance "In this scenario, we could only observe the strong isotropic growth of the root radicle without a specific orientation of CMTs (Figure 1A) » does not match with what is shown on Figure 1A. More importantly, the authors should provide evidence of CMT orientation before and during radicle outgrowth to support their claim (this could be down on fixed tissues, or with existing, even published, data). Last the authors, should also discuss growth anisotropy and growth direction (not only growth rate) to show that the CMT orientation emerges from a conflict of growth rate, and not from a conflict of growth direction (see e.g. Rebocho and Coen). This is necessary especially because the authors claim that "anisotropic growth of the root emerges from initially uniform isotropic cell expansion", hence growth anisotropy needs to be quantified. This should be an easy fix since all the relevant data are present on the video files.

3) radicle vs. root: The transition between the initial symmetry breaking event and the anisotropic growth of the root is a bit problematic to me: we are not looking at the same cells/stage anymore. It's almost as if there were two papers in one. I'm wondering whether the Heisler model could be tested at the early stages of radicle emergence, i.e. assuming that differential growth prescribes maximal membrane tension around the emerging radicle, wouldn't PIN polarize towards the radicle (assuming PIN is recruited on the most tensed membrane, because tension traps it there)? This would at least provide a link between the two parts of this study. Furthermore, this would allow the authors to test how robust (or more likely, how "unrobust") is a 100% stress-derived PIN polarity model for root growth, leading to the exploration of alternative hypothesis (phosphatase model).

4) Robustness of the model: The phosphatase model with the addition of the stem cell division rule can reproduce observed PIN patterns. This is a nice hypothesis, but without experimental support for it (i.e. PP2A phosphatases are certainly involved, and there is experimental support for that, but it is still unclear how central their role is). The simulations show that this hypothesis is plausible, but one could probably envision many other mechanisms. Thus, in absence of molecular support for the hypothesis, the central question is that of robustness. Given the number of parameters in the model, one could likely find a parameter space in which the model is robust. The robustness of the model is tested with different embryo geometry and "in a plausible range of parameter values". This part should be expanded. In particular, for which values is the model not robust anymore? The multiple tests at the end of the result section provide support for the robustness of the model. I would conclude that the model is robust only at the end of the results, and not before those tests.

Reviewer #3 (Recommendations for the authors):

Great study! In my opinion, it just requires some polishing and restructuring.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A coupled mechano-biochemical model for root meristem morphogenesis" for further consideration by eLife. Your revised article has been evaluated by Detlef Weigel (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

All three reviewers are somewhat disappointed by the changes made by the authors. While a major revision was called for the authors seemed to have mostly made the easiest textual changes rather than going into certain biological details, or answered certain reviewer comments while not making corresponding changes in the text. English language and grammar are still not of high quality and at places very poor and limiting understandability.

We therefore ask for another round of revision in which you address all remaining issues, particularly the points raised with regards to biological details.

Reviewer 1:

Title/Abstract/Discussion

Although no claim of self-organization is made within the title, also the word morphogenesis or the statement that their model explains root shape is overselling what the authors can explain with their model. The model in its current form explains only the elongated shape of the root from the initial mechanical symmetry breaking and auxin patterning, but not its specific wedge shape nor the specific switching between division patterns close to the QC that sets up the different tissue layers. I suggest to replace morphogenesis/shape with (polarity) patterning or something in that direction. Discussion line 434/435: please remove that the model explains tissue patterning, as it does not as the authors describe themselves that they need certain rules to get the cell division patterns and hence the organization of tissue types right near the QC.

Response to comments:

– Author answer to point 27 by this reviewer: the authors should write their answer also explicitly in the discussion: that the model requires extension in terms of adding remeshing before it is suited for studying tropisms

– Author answer to point 30 raised by this reviewer: also write this explicitly in methods

– The authors now show that mechanics/AF is necessary for correct PIN and auxin patterning. First, it is not entirely clear whether mechanics were removed from these simulations (Figure 2 Suppl 7 from the start or after initially running the full model). Please clarify. Second, this nice result deserves some more attention, discussing how mechanics define the axis and PIN dynamics the polarity in the text!

Reviewer 2:

Rather than going into the particularities of mechanics, PIN delivery, and the roles of different parts of the cytoskeleton in this, as suggested by the reviewer, the authors have simply rephrased matters into a generic "anisotropy factor". I suggest that at least some effort into discussing the underlying biology in more depth is undertaken.

Reviewer 3:

It is recommended that the authors have another look at the points raised earlier and address these appropriately. As an example in their current response they indicate that simulation is a complete PIN KO (which would be embryonically lethal) yet in the paper it still states pin1 mutant. Also no appropriate response to and explicit incorporation of into manuscript of the fact that in the model columella PIN levels are predicted to be much lower than observed experimentally is given. Etc. It’s a nice model, so there is no reason to hide limitations, all models have them.
