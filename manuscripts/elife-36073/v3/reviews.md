# Peer review - Round 1

Editors:
- Mohan K Balasubramanian, University of Warwick United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.36073.030](https://doi.org/10.7554/eLife.36073.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: a previous version of this study was rejected after peer review, but the authors submitted for reconsideration. The first decision letter after peer review is shown below.]

Thank you for submitting your work entitled "Positive feedback between contractile ring myosin and ring-directed cortical flow drives cytokinesis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Michael Glotzer (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife at present.

The reviewers appreciated the novel imaging and computational approaches you are using to understand mechanisms of cytokinetic force generation. The reviewers also found the premise that cortical flow of myosin together with existing myosin in the furrow regulates the rate of furrow contraction interesting. However, a number of issues were raised. These include 1) inconsistencies with what is known in the literature (some experiments with Rho pathway and Nop1 mutants can address these), 2) issues with the theoretical framework and terminologies used (raised by reviewers 1 and 2, which may need experiments and rewriting), 3) aspects of the data fitting and conclusions regarding cortical flow (reviewer 1; may require reanalysis / reconciliation), and 4) referencing (reviewers 2 and 3; should be easily fixed).

If you feel you can address the issues raised with experiments and rewriting / analysis, we will be happy to consider a revised version or as a new submission. In both cases, we will send the paper to the same reviewers.

Reviewer #1:

Cleavage furrow ingression during animal cytokinesis is driven by constriction of the actomyosin contractile ring. While major components of the contractile ring and key regulators for its assembly and constriction have been identified, our mechanistic understanding on how it generates force is limited. In their previous publication, based on the observation that the rate of the ring contraction is largely constant and proportional to the initial size of the ring, the Oegema group proposed a 'contractile unit' model, which assumes a presence of a contractile unit with a fixed initial length, which retains myosin while it shortens.

In this manuscript, the Oegema group studied further details of the mechanism of the ring constriction by precisely measuring the flow and total amount of cortical myosin as well as the myosin in the ring during the ring constriction. Based on these analyses as well as the results of laser micro-surgery and genetic manipulations, they propose a mathematical model with three parameters, which was demonstrated to be useful to explain the effects of a perturbation (depletion of Rho-kinase). The quality of image analysis, especially the 4D mapping of the cortical flow, is extremely high with striking number of video data analyzed. However, there are major problems to be addressed before publication.

1) Logic to choose the feedback model instead of the retention model.

The authors' logic for throwing away the retention model is not clear. The similarity between the time courses of the ring-directed cortical flow and the mean ring myosin or anillin per unit length, and the behavior of the ring myosin after FRAP are the observations on which they were based. Good fitting to exponential curves with a common time constant is interesting and is consistent with the cortical flow feedback model. However, the data are not strong enough to tell exponential from hyperbolic curves. The retention model predicts that the ring myosin per unit ring length is proportional to the inverse of the ring radius (∝1/R) (Figure 4C). Under the constant rate of ring constriction, this means that the ring myosin per unit ring length is proportional to 1/(Runit – v∙t) (t: time, v: rate of ring constriction measured by radius), a hyperbola. With the value range used for Figure 3 and 4 (3 to 4-fold increase), it is almost impossible to distinguish an exponential curve from a hyperbolic one. Indeed, as a simplest example, a set of (x, y) calculated by y=1/(1-x) can be fitted with an exponential curve very well (as we can see by an R script below). The authors should explain why the data support exponential increase better than hyperbolic one.

What data tell us are the largely fixed total amount of ring myosin (with limited exchange with flanking cortex or cytoplasm) and the constant overall cortical flow into the division plane. These two are balanced by some events in the division plane or in the ring (this remains a big black box mainly due to missing direct observation of the cortical flow in the division plane). I appreciate that it was possible to make a mathematical model based on the positive feedback and that it could be fitted to two different conditions (control vs. rho kinase depletion). However, considering that the data don't indicate increase of the total amount of ring myosin, it is difficult for me to understand the necessity of the positive feedback.

2) Logic to disregard accumulation in the division plane, loss by disassembly and turnover with the cytoplasmic pool.

As far as I understand, the only reasoning for disregarding "accumulation in the division plane" and "loss due to disassembly" (Figure 3C) is the similarity between the time course of the ring-directed cortical flow and the time course of ring myosin and anillin per unit length. However, this argument assumes that there is no turnover of myosin with the cytoplasmic pool at the division plane and the ring and that the flow within the division plane is uniform and constant (no accumulation). The authors claim that the result of FRAP excludes the exchange of the ring myosin with the cytoplasmic pool. However, their argument "If ring myosin were turning over due to exchange with cytoplasmic myosin, we would expect the FRAP curve to approach the control curve and the difference between the FRAP and control curves to disappear" is true only if all the ring myosin is exchangeable with the cytoplasmic pool and the exchange occurs rapid enough. This assumption is too strong (a kind of straw man argument). The absence of complete recovery simply tells us that there is a non-exchangeable population in the ring myosin. Moreover, indeed, the difference is getting smaller. The basis for the constant cortical flow in the division plane is unclear.

3) Laser dissection.

The authors performed laser dissection experiments (Figure 2) to assess the influence of the cortical resistance on the rate of ring closure. However, it doesn't seem to be sufficient/complete to draw any firm conclusion. It is not clear whether they are comparing the parallel and perpendicular cuts on their effects on the ring constriction. Only the absence of the effect of the parallel cut was mentioned. The cortical flow is not spatially uniform (Figure 1), implying that the cortical tension is also non-uniform. Then, don't we need to consider the relative positioning (angle and distance) between the ring and the cut? Is the lesion big enough? Even after the cut the ring can still be connected to the polar cortex via the unaffected zone of cortex. What would happen if a whole polar cortex is completely separated from the other part of the cortex and the ring? The rationale for the purple line in the Figure 2C "Expected rate if […]" described in the Materials and methods "The cortical opening after ablation was approximately 35μm2; this translates into an additional reduction in ring radius by ~0.8μm, if the cortical surface tension dominates the ring closure rate." needs more detailed explanation.

(R script to demonstrate the difficulty in distinguishing exponential curve and hyperbolic curve)x <- (0:16)/20y <- 1/(1-x)model <- nls(y~a+b*exp(c*x), start=list(a=1, b=1, c=1))xx <- (0:80)/100z <- predict(model, newdata=list(x=xx))plot(x, y, ylim=c(0,5))lines(xx,z)coef <- summary(model)$coefficients[,1]fit = sprintf("y=%.4f+%.4f*exp(%.4f*x)", coef[1], coef[2], coef[3])legend("topleft", legend=c("y=1/(1-x)", fit), pch=1, lty=c(0,1), pt.cex=c(1,0))

Reviewer #2:

This manuscript describes the kinematic analysis and mathematical modeling of the behavior of contractile ring components during cytokinesis. The basic assertion is that cortical myosin flows into the furrow region during ingression and these flows lead to increased accumulation which drives more rapid ingression as furrowing proceeds. Within its technical limitations, this work is carefully performed. It makes its underlying assumptions clear, and is supported by a model that appears consistent with these assumptions. However, there are fundamental problems with these assumptions and significant technical limitations. Ultimately, I do not find the central point of the manuscript convincingly demonstrated.

Concerning the technical weakness: The majority of the data in the manuscript is based on measurements of cortical components on the flatter parts of the embryo. "Cortical flow could not be monitored in the division plane or at the cell poles, due to their high curvature." Thus the part of the cleavage furrow where contractile ring components accumulate to the greatest extent are not detected with the same spatial or temporal resolution. Thus there is an intrinsic limit to the authors ability to track flow of cortical components from the surface and account for its accumulation at the furrow tip. This could be addressed by analyzing cell division of blastomeres that furrow in the imaging plane.

The manuscript extensively discusses a concept they call cortical surface area. This is a mixed metaphor that appears to include aspects of the cortex and the plasma membrane. The authors state, "New cortical surface could be gained uniformly, immediately behind the contractile ring, or at the cell poles" and cite a number of publications that assess the behavior of the plasma membrane during cytokinesis. However, this concept is flawed. As cytokinesis proceeds, the membrane surface area must expand in order for the cell to retain integrity. While the plasma membrane is by definition continuous and uninterrupted, the cell cortex is different, it need not cover the entire membrane to a constant "depth". Furthermore, fluorescence imaging reveals large inhomogeneities in the cortex and, unlike membrane lipids, cortical components can associate and dissociate.

Another major, central weakness is that the manuscript primarily considers two models for accumulation of myosin in the furrow: retention and ring-directed flow. While these mechanisms likely contribute, they represent an incomplete view of the mechanisms by which components accumulate in the furrow. The authors appear to assume that contractile ring components are recruited at a specific time and then reorganized on the cortex. Indeed, the text states, "cytokinesis initiates when spindle-based signaling activates RhoA on the equatorial cortex leading to the abrupt recruitment of contractile ring components." Presumably, they also imagine that additional components are recruited at poles to replace the material that flows toward the furrow. However, this view is inconsistent with extensive analysis of the mechanism of Rho-dependent assembly of the contractile ring. RhoA is active throughout cytokinesis, as indicated by continual association of a RhoA biosensor, which is most concentrated at the furrow. Unfortunately, this key region largely falls outside of the part of the embryo the authors image at high spatial and temporal resolution. Given what is known about RhoA and its effectors, there is no reason to posit that during the course of furrow ingression, active RhoA does not continually activate its effectors and induce recruitment of contractile ring components throughout the progression of cytokinesis. Indeed, the observed increases in ring components may follow the increase in the concentration of active RhoA at the furrow.

The authors suggest that their data excludes recruitment of myosin from the cytoplasm, but the evidence is unconvincing (Figure 4C, subsection “Component levels and fluorescence recovery after photobleaching of the division plane support constriction rate acceleration due to ring-directed flow versus component retention”, second paragraph). For example, the FRAP data is consistent with the furrow tip containing a pool of myosin that has lower mobility. The "recovery" after bleaching could reflect de novo recruitment on top of the slowly exchanging bleached myosin. In addition, there is little evidence of flow of unbleached myosin into the ring, which would be predicted from the author's model.

The authors find a correlation between the rate accumulation of myosin in the ring, and the rate of constriction. There is no evidence that this correlation reflects a causative relationship.

Consistent with the previous point, evidence in the literature contradicts the authors explanation that cortical flows of myosin from regions flanking the furrow are required for the proposed exponential increase in contractile ring myosin that speeds up the rate of ingression. Specifically, C. elegans embryos deficient in NOP-1 are significantly depleted of cortical accumulation of contractile ring components outside the of the equatorial/furrow region. However, these furrows ingress with near wild-type kinetics, indicating that efficient furrow ingression does not require these major flows of contractile ring components. Rather, it suggests the existence of an alternative mechanism that provides for a time-dependent increase in contractile ring components.

Conversely, embryos that are defective in centralspindlin-directed RhoA activation, do contain cortical myosin that appears to flow in the proposed manner, yet such embryos ingress partially and slowly, suggesting that flow-mediated concentration of contractile ring components is insufficient to generate the proposed behavior of the ring.

The authors state "The broad conservation of this property, which allows cytokinesis to complete in a temporally restricted cell cycle window, suggests that feedback between contractile ring myosin and ring-directed cortical flow will be a broadly conserved property of contractile rings in animal cells." This would imply that cells that lack ring-directed cortical flow will exhibit aberrant timing of ring closure. However as mentioned above, analysis of NOP-1 deficient embryos violates this conjecture.

The authors discuss the concept of astral relaxation: "This differential response of the polar cortex to ring-generated tension, which results in a flow of myosin and other cortical components towards the cell equator, is consistent with the idea of polar relaxation hypothesized in early conceptual models of cytokinesis." They fail to mention or cite that astral relaxation has been experimentally documented in the early C. elegans embryo. Indeed it has been demonstrated that a posterior directed spindle directs anterior-directed flow of cortical components that self organize into a furrow (PMID 17669650). Importantly, this anterior furrow is entirely dependent upon the protein NOP-1 (PMID 22918944).

Reviewer #3:

The manuscript from Khaliulin et al. investigated the contribution of cortical flow in maintaining constant rate of ring constriction during cytokinesis in worm embryos. Both de novo actin/myosin assembly at the division site and cortical flow of components to the cleavage furrow are involved in cytokinesis. However, it remains controversial about the relative importance of each pathway. But I think the paper still need some minor revisions to be acceptable for publication.

1. Due to no cell cortex in yeasts but the ring constricts at a constant rate (Pelham and Chang, Nature, 2002), the references of Wu and Pollard 2005 paper in the Introduction and Discussion are somehow misleading. In fission yeast, myosin-IIs mostly retain in the ring during its constriction, they are also highly dynamic by exchanging between the ring and cytoplasm. The similarity and difference between Wu and Pollard, Carvalho et al, and the current work should be discussed.

2. In Zhou, M., & Wang, Y. L. (2008), "Distinct pathways for the early recruitment of myosin II and actin to the cytokinetic furrow" (Mol Biol Cell, 19(1), 318-326), it is found that myosin-II is recruited to the furrow mainly by de novo assembly, but not cortical flow, during early cytokinesis in mammalian cells. This and other similar works on cortical flow and de novo assembly should be cited and discussed.

3. A figure supplement showing the cortical flow map at cell poles before and during ring constriction will be useful.

4. The terms "cortex surface" and "surface gain" are confusing. Because the plasma membrane was not directly tracked, it should be make clear what you mean here. Otherwise, casual readers may think the plasma membrane is inserted at cell pole, which is likely, but not tested here.

5. The Materials and methods section is not clear regarding how background fluorescence was subtracted. Which region was used as the background?

6. The reference citations are not consistent, sometimes multiple authors from the same paper are listed.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for resubmitting your work entitled "A positive feedback-based mechanism for constriction rate acceleration during cytokinesis in C. elegans" for further consideration at eLife. Your revised article has been favorably evaluated by Anna Akhmanova as the Senior Editor, Mohan Balasubramanian as the Reviewing Editor, and three reviewers (including Michael Glotzer).

The manuscript has been improved but there are several remaining issues that need to be addressed before acceptance, as outlined below.

The referees have returned their comments and I have discussed the comments with the Senior Editor and we have compiled this decision letter with all substantive points raised by the three referees.

In particular, I have taken the step of providing the full list of comments so that the counter arguments to your model for mechanism of acceleration of cytokinetic ring contraction and the role of myosin II accumulation via cortical flow are fully captured.

In light of the fact that all three referees have concurred that the imaging data are among the best in the field of worm cytokinesis and that I believe you are proposing a striking and provocative new model for aspects of cytokinesis, we are interested in publishing your work, and invite you to submit a revision. In the discussions between referees, it was highlighted that the paper was worthy of publication, but that the models need to be considered more critically.

We would like you to rewrite the paper significantly, based on these comments, as well as perform a straight-forward experiment.

One of the referees has raised the unsatisfactory resolution of the current study vis-à-vis the previous work from your laboratory (Carvalho et al., 2009) (Points 10 and importantly 11). The Senior Editor and I concur with the points the referee has raised. We believe a clear statement of your current position is consolidating the Carvalho paper and the current study will be very valuable for the field and will prevent any confusion in the field.

Also, I believe one experiment, of treating 1 and 4 cell embryos with LatA, as a test of your model is required (point 11).

Point 9 below also requires special attention. The exponential vs. hyperbolic accumulation of components in the ring cannot be easily distinguished and the referee has detailed their concern. Please clarify the limitations of your analysis.

Please also pay attention to the use of terminology, which have been raised by all referees (cortical surface area, cortical area, naive cortex), raised by the referees throughout the comments.

Below, I mention what needs to be done for each point.

Although I think I can decide on any submitted revision, I might call upon one of the referees, if required.

Please find below the consolidated comments of the three referees and my recommendations.

1) The revisions to the manuscript have clarified their model so that readers can better understand what the authors claim to demonstrate. I remain unconvinced of the authors model. My concerns are due to the fact that the manuscript is largely based on an inference of cortical compression.

I want to first re-state that the data shown are carefully obtained. The measurements of cortical flow are of interest. The authors provide evidence that the rate of furrow formation is limited by internal viscosity in the contractile ring, which is a novel insight and an important point.

Overall, I remain unconvinced by the author's interpretation of their results. There is some value in their quantitative model, though (1) it is not well constrained, there is no reason why the flow has to be the source of positive feedback and (2) it has not been extensively tested experimentally. However, if the authors want to publish their interpretation, I have no strong objection, particularly in eLife where readers can readily access the reviews that indicate that experts in the field do not subscribe to their interpretation of their results. Notably, the authors and I communicated following the first version. This communication has lead to a more clear description of their model. Yet during that process I communicated the gist of the comments below, yet they remain unresolved in this version. Specifically, in the previous version, the manuscript gave the impression that cortical flows delivered myosin into the furrow region, thereby accelerating ingression, flows, and myosin accumulation through a form of positive feedback. Now, the authors have clarified their interpretation as follows:

a) The amount of cortical surface area that flows into the furrow region exceeds the surface area of the division plane.b) As a consequence of (1) and an unstated assumption that cortical surface area is not disassembled, the authors infer that cortical surface area is compressed. There is no direct evidence for cortical compression except at the very earliest stages of furrow formation. Interestingly the rate of flow at the stage where compression is observed is 2-3x lower than that during furrow ingression (Figure 1B vs. 3A).c) The total cortical surface area is inferred to increase exponentially and it parallels the increase in ring components.d) Yet, the myosin that flows into the furrow region is not a major contributor to ring myosin, rather it largely disassembles. Indeed, in en face views of the division plane, there is no detectable flow of myosin from the "exposed" cortex to the ring.e) However the flow of cortex is proposed to provide additional, initially "naive", cortical surface area that is then patterned by RhoA (Figure 7), and it is this exponentially increasing cortical surface area that leads to exponentially increasing levels of ring myosin. This begs the question, what is "naive" cortex?

(Editors’ recommendation: rewrite significantly for clarity)

2) At the core of the issue with this model is inference of cortical surface area compression. First, the authors claim that cortical compression can be readily inferred from the difference between the amount of cortical flow into the division plane and the area of the division plane. Yet, the actomyosin cortex is dynamic, in addition to compressing and expanding, it can assemble and disassemble. Indeed, the manuscript shows that at the poles, cortical surface area is created as the cortex flows into the furrow region. And, myosin – a key component of the cortex – is largely assumed to be lost as the furrow flows into the division plane (see point 3). Thus, while cortical compression is possible, cortical disassembly is another possibility, which is not given sufficient consideration. In fact it is a strong possibility given that there is loss of a key component of the cortex, myosin.

(Editors’ recommendation: rewrite significantly for clarity)

3) Furthermore, the authors have not explained why "naive cortex" would be required for the zone of active RhoA to drive an increase in myosin accumulation?

(Editors’ recommendation: rewrite significantly for clarity)

4) Given that ARP-2/3 nucleated actin is likely a nucleator of some of the actin in the cell cortex, it is notable that its depletion does not dramatically affect the rate or extent of furrow ingression in otherwise WT embryos, as has been shown previously (PMID 22226748). This raises the follow-up question: what is "naive" cortex in ARP-2/3 depleted embryos?

(Editors’ recommendation: rewrite significantly for clarity)

5) In the author's rebuttal letter (reviewer 2, fourth response) the authors state, "The reviewer would propose that there could be another source of positive feedback that controls myosin accumulation (for example some type of ring intrinsic feedback loop involving Rho-based signaling), and that exponential accumulation of myosin arising from this as yet un-described feedback loop could, in turn, control the constriction rate and the rate of cortical compression. We do not disagree that this could be the case." Positive feedback in RhoA signaling during cytokinetic processes has been demonstrated, (PMID 26479320), and there is evidence for a mechanism in which RhoA might generate positive feedback through the recruitment of centralspindlin and its activation of the RhoGEF ECT-2 (PMID 26252513).

(Editors’ recommendation: rewrite significantly for clarity)

6) Given the topic of this manuscript, it is surprising that the authors do not mention that local RhoA activation is sufficient to induce furrow formation (PMID 27298323) and all of the literature concerning the mechanism of RhoA activation during cytokinesis.

(Editors’ recommendation: consider discussing this paper)

7) The authors state, "We propose that, due to polar relaxation, the compressing cortex pulls naive cortex not patterned by the initial round of RhoA signaling, into the Rho zone." Here the authors are generating confusion between terms that have a different historical meaning. Polar relaxation was used to describe a mechanism by which astral microtubules might induce a net increase in equatorial contractility by the local inhibition of contractility at the poles (polar relaxation). Here, they are discussing how existing equatorial contractility induces flow of cortex away from the poles. These terms are already sufficiently confused in the literature, it would be better to avoid adding to it.

(Editors’ recommendation: rewrite significantly for clarity)

8) One paper published during their revision is quite relevant: PMID: 29146911. DOI: 10.1038/s41467-017-01231-x. I suggest that the authors cite and briefly discuss the paper in their final manuscript.

(Editors’ recommendation: consider discussing this paper)

9) Exponential/hyperbolic accumulation.

In Figure 5, the authors compare exponential curves and hyperbolas for fitting with the experimental data and conclude that exponential curves fit better. However, it is unclear whether their comparison is fair. For fitting with the data of mean fluorescence per unit length with an exponential curve (Compression feedback), three parameters, i.e., the amplitude, the time constant and baseline can be adjusted. On the other hand, for fitting with a hyperbola (Retention model), it is unclear what the formula for R(t) looks like and what degree of freedom was allowed.

As I pointed out in the previous reviewer comments, clear distinction between the exponential curve and hyperbola is not trivial. The authors' own data and interpretation demonstrate this difficulty. First, in Figure 3C, "Cortical compression (rate per unit ring length)" is fitted with an exponential function. However, this quantity dAcompdt1R should follow a hyperbolic increase in time since the first term, dAcompdt, is largely constant (Figure 3B 'Normalized Surface Area Flux') and the second term, 1/R, is an inverse of a linearly decreasing function of time (Figure 1A). Second, in the same panel, "Ring shrinkage rate per unit length (-dRdt1R)" is also fitted with an exponential curve. However, this quantity should also be hyperbolic for the same reason (-dRdtis constant most of the time during furrow ingression Figure 1A). These examples nicely demonstrate the difficulty in distinguishing between exponential and hyperbolic changes by curve fitting with a set of data that are not really suitable. The authors' approach doesn't have sufficient power to discriminate between possible theories.

(Editors’ recommendation: rewrite significantly for clarity as well as discuss the limitation of the curve fitting approaches you have taken)

10) Exchange of ring myosin with cytoplasmic pool.

I am really confused with what the authors are actually thinking about the exchange of myosin with the cytoplasmic and cortical pools. Based on the whole division plane FRAP experiment in Figure 6, they exclude the exchange of the ring myosin with cytoplasmic myosin. On the other hand, in the schematic in Figure 4, the recruitment of cytoplasmic myosin to the Rho zone is depicted as the major source of the increase of the cortical myosin in the Rho zone. Although it was not explicitly stated in mathematical modeling, myosin on the cortical flow within the Rho zone and myosin accumulated at the contractile ring behave differently as to new recruitment and removal by disassembly. In the FRAP in Figure 6, both of these myosins, as well as myosin on the 'naive cortex' in the division plane, were photobleached. Recovery seems to have started at the contractile ring instead of the flowing cortex outside of the ring. The simplest explanation would be that there is an exchange of myosin at the ring.

A constant level of per-unit-length bleached myosin is a basis for their compression feedback model. However, bleached myosin calculated by the two formulas made by exponential fitting is not constant. Contrary to their description (subsection “Fluorescence recovery after photobleaching of the division plane is consistent with the Compression Feedback model”, last paragraph), the two curves are getting closer (see graphs that can be generated by running an R script at the bottom). This point was clearer in Figure 4C of the original submission. If we apply the same logic as later in the aforementioned paragraph, the data indicate that the recovery is at least partially due to the exchange with cytoplasmic myosin. I don't understand why they could assert "We also note that, consistent with our prior observations at the 4-cell stage (Carvalho et al., 2009) we did not observe evidence of turnover of ring myosin due to exchange with myosin in the cytoplasm."

(Editors’ recommendation: rewrite significantly for clarity and explain limitations)

11) Consistency with Carvalho 2009.

The authors' argument in Figure 6B is valid to exclude the retention model without any exchange at the ring. However, the same logic also strongly argues against the model proposed by Carvalho (2009), which excludes both the exchange of the ring myosin with cytoplasmic myosin and with the nearby cortex. The tornado-shaped non-recovery zones in the kymographs were explained by the closure of the ring and slow exchange within the ring in the absence of the exchange with the cytoplasm nor delivery by flow from the flanking cortexes. However, if the current model is correct, the flow from the flanking cortex should cause a gradual recovery in the tornado-shaped zones in the kymographs. In other words, the current model is not consistent with the data by Carvalho (2009).

In Figure 3—figure supplement 4, the authors quantified the per-unit-length amount of myosin in 4-cell stage division. This should be essentially equivalent to Figure 4D in Carvalho (2009), from which they had concluded that the per-unit-length amount of myosin in the ring is constant (note: this is reproduced as Author Response Image 2 in their reviewer response, hiding the latter half of the time scale where the drop was observed before the sudden 1.3-fold increase at 10 µm perimeter. In addition "In contrast, we observed a ~1.3 fold increase for all three components." is also misleading as they mentioned the 1.3-fold increase only in the last few µm, sticking to the constant per-unit-length level. Additionally, the point of transition is 18 µm in Figure 4D of Carvalho (2009) but 25 µm in their rebuttal. It is not clear why at a glance they look different (or the author could conclude differently). Are they based on the same set of image data? Or, was the recording newly performed? How do they look if they are plotted with the same x-axis (the perimeter of the ring or fraction of ring closure)?

Simply speaking, the major conclusions in Carvalho (2009) are inconsistent with those in current manuscript. There are 4 possibilities:a) Divisions in 1-cell stage and in 4-cell stage are different.b) There is no such difference. The data or interpretation in Carvalho (2009) was wrong. The current model is correct.c) There is no such difference. The current model is wrong. The old model was correct.d) There is no such difference. Both the old and new models are wrong

The authors should clarify which is the case. If b) is the case, detailed point-by-point explanations will be essential as to which data/interpretation in the previous paper still stand or don't stand anymore.

To distinguish between these possibilities, repeating latrunculin A treatment during furrow constriction at 1-cell and 4-cell stages using eggshell permeabilization by perm-1(RNAi) would be highly informative. In Carvalho (2009), insensitivity of the 4-cell division to latrunculin A added during furrow ingression provided a support for disregarding the importance of turnover.

(Editors’’ recommendation: Perform the LatA treatment experiment as well as clearly state what exactly your position is in terms of this manuscript vs. the Carvalho manuscript)

12) Inconsistency between the scheme in Figure 4 and their own observation (Naive cortex?).

The model doesn't match with what was observed by the authors. It is ambiguous what the 'naive cortex' is. In the scheme in Figure 4A left box, it is placed between the equatorial Rho zone and the polar cortexes and treated as empty boxes without myosin. The only route of recruitment of myosin to the cortex is the direct recruitment of myosin II from the cytoplasm in the Rho zone. However, this picture is not consistent with their own observations.

In Figures 1 and 3, they observed the flow of myosin II in the cortical regions at the surface of the embryos, which largely correspond to the regions marked in grey in Figure 4 (and the green Rho zone before furrow ingression starts). Myosin DOES exist in these regions of "naive cortex". The authors may argue that myosin in these regions is inactive. However, at the beginning of furrow ingression (Figure 3, t/ttck -0.1 and Figure 1t/tck 0.2 'bottom'), the gradients are observed in regions wider than the ~10 µm wide 'Rho zone'. In later stages, the authors attribute the velocity gradients in the regions flanking the furrow to a projection artifact (dotted segments in Figure1) although it is not very clear how convincing this interpretation is. In the regions where the flow is represented by a solid line, the velocity is largely constant. However, an absence of compression doesn't necessarily mean that myosin is inactive. The tension generated by myosin might just be balanced. Indeed, laser ablation caused outward flows in all the directions (not limited to the direction towards the furrow), indicating that the 'naive cortex' is under active tension although it would be lower than that in the Rho zone.

(Editors’ recommendation: rewrite significantly for clarity)

13) Inconsistency between the mathematical model and the scheme in Figure 4

In the schematic in Figure 4, recruitment of myosin from the cytoplasm is depicted as the major route of the increase in the total amount of myosin in the Rho zone. However, in the mathematical model, a key assumption is that the mass of cortical myosin is conserved while it flows (formula 20). There is no term that corresponds to the recruitment from the cytoplasm.

(Editors’ recommendation: rewrite significantly for clarity)

14) Lack of the effect of geometry change by furrow constriction, or the mechanism for coupling removal of myosin with furrow constriction.

Simply due to the geometry change, even without new recruitment of myosin either via cortical flow or from the cytoplasm, furrow constriction results in an increase of the per-length-amount of myosin if there is no removal of myosin coupled with the disassembly of the contractile units. However, this fundamental fact hasn't been properly incorporated in their mathematical model.

The consequence of this process is mentioned and depicted in the right box of the Figure 4A "Ring shortening is coupled to disassembly and does not change the per unit length amount of ring myosin". In Figure 4B, in box 3, under the lead "The per unit length rate of ring disassembly is proportional to the per unit length amount of ring myosin", the formula (24) is shown. However, this formula is about the relationship between the per unit length amount of ring myosin and the per unit length rate of ring constriction (instead of the per unit length rate of ring disassembly). The caption can be true only when the ring disassembly is proportional to the ring constriction. In their model, this is achieved by neglecting the effect of geometry change due to furrow constriction while they are discussing formula 18 to 23, and later on by using Mring as equivalent to the per unit length amount of ring myosin without properly explaining that their model doesn't include a mechanism for coupling constriction and disassembly, which is not trivial and was a key discovery in Carvalho (2009).

(Editors’ recommendation: rewrite significantly for clarity)

15) The velocity of flow of naive cortex into the Rho zone.

The authors' theory predicts a linear relationship between vflow, the velocity of flow of naive cortex into the Rho zone, and Mring, the total per-unit-length amount of ring myosin (formula 22). Although, mathematically, vflow(t) is the speed of the flow at the boundary of the Rho zone, considering the continuity of the flow at the boundary of the Rho zone and largely uniform flow, it is reasonable to interpret vflow(t) as the velocity/speed of flow of naive cortex. In Figure 4, this is indicated by growing arrows labeled "Cortical flow" on the 'naive cortex'. However, the data in Figure 1 and 3 don't show such behavior. Instead, the flow seems to show rapid increase around t/tck~0 and gradually slows down between t/tck>0.2. It will be informative if the top and bottom speeds of cortical flow are plotted against time. Anyway, this pattern is inconsistent with the theoretical prediction. In this case, their favourite trick to convert a constant quantity into an exponentially increasing one by dividing by the ring radius wouldn't work well since the radius that can be used here is the radius at the boundary of the Rho zone, which only decreases towards 5 µm, instead of the ring radius, which decreases towards 0 µm.

(Editors’ recommendation: rewrite significantly for clarity)

16) 'Rho zone'.

It is not clear what exactly the 'Rho zone' is especially after the furrow has deepened (the distance from the embryo surface to the contractile ring is larger than 5 µm). In the mathematical model, they assume that w is a constant. However, this is not realistic. The actual width of the distribution of active Rho in the cell is likely to be broader in the beginning and become narrower. The word "ring" stands for the contractile ring in most places while in some places it refers to a broader zone used for quantifying myosin (e.g. Figure 6A, the zone between the two boundaries marked with dotted lines). In the latter case, the 'ring' largely overlaps with the 'Rho zone' but not in the former case.

(Editors’ recommendation: rewrite significantly for clarity)

17) Feedback?

The authors argue that exponential increase suggests a positive feedback. However, this is not necessarily true (even if their interpretation of exponential increase were true). For example, under an optimal condition, bacteria grow exponentially. Usually, this is not explained by a positive feedback loop. To confirm a feedback loop, an experiment to perturb a key step in the loop should be performed.

(Editors’ recommendation: rewrite significantly for clarity or perform an experiment)

18) "Cortical surface".

I support reviewer #2's original point about the terms "cortical surface" or "cortical surface area". The authors' rebuttal is not convincing. In 50's, the current concepts of "plasma membrane/cell membrane" and "cell cortex" were not established yet. The fluid mosaic model was established in 70's. The "membrane" in Swann and Mitchision (1958) refers to a combination of the lipid bilayer and the underlining cytoskeletal network.

The markers listed are all added from the medium and attached on the cell surface (except for Dan's pigmented granules). The relations between these surface markers and the cortical cytoskeletal network haven't been clarified and can be variable. The expansion (an increase of the distance between the markers) can be caused between the markers that are not anchored to the cortical cytoskeleton by insertion of new membrane lipid bilayer. If markers are somehow anchored to the cortical cytoskeleton, the expansion can also be caused by relaxation of the cytoskeletal network (or radial pull by the neighboring cytoskeletons).

The terms "cortical surface" and "cortical surface area" are confusing. The latter has been widely used to describe the geometry of brains. The usage of it in the context of cytokinesis seems to be a recent invention by the authors. At least, this word doesn't appear in Dan (1954) nor in Swann and Mitchision (1958) although they used "cortical layer", "cortical gel" etc.

In most of the cases in this manuscript, just "cell cortex" instead of "cortical surface" seems to be appropriate.

# an R script to plot unbleached myosin based on the fitted formulas in Figure 6Ct <- (0:100)/100y1 <- 0.22*exp(2.8*t)+0.78y2 <- 0.24*exp(2.8*t)-0.07y3 <- y1-y2quartz(width=4, height=4.5)plot(t, y3)plot(0,0, xlim=c(0,1), ylim=c(0,4.5), type="n", xlab="time", ylab="signal per length", xaxs="i", yaxs="i")lines(t, y1, col='magenta')lines(t, y2, col='green')lines(t, y3)

(Editors’ recommendation: rewrite significantly for clarity)
