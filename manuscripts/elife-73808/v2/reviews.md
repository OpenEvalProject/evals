# Peer review - Round 1

Editors:
- Lydia WS Finley, https://ror.org/02yrq0923 Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73808.sa0](https://doi.org/10.7554/eLife.73808.sa0)

This paper describes the derivation and validation of a coarse-grained model to measure mitochondrial metabolism at cellular and subcellular resolution by exploiting fluorescence lifetime imaging of NADH. This technique is applied to mouse oocytes subjected to a variety of metabolic stresses and to human tissue culture cells, revealing spatial gradients in mitochondrial NADH oxidation. This method represents an exciting new approach to quantifying mitochondrial electron transport chain rates and provides for the first time a method to study mitochondrial metabolic flux with subcellular resolution.


---

# Peer review - Round 1

Editors:
- Lydia WS Finley, https://ror.org/02yrq0923 Memorial Sloan Kettering Cancer Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73808.sa1](https://doi.org/10.7554/eLife.73808.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Coarse-grained model of mitochondrial metabolism enables subcellular flux inference from fluorescence lifetime imaging of NADH" for consideration by eLife. Your article has been reviewed by 4 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jason W. Locasale (Reviewer #2); Edmund J. Crampin (Reviewer #3).

We are sorry to say that, after consultation with the reviewers, we have decided that your work will not be considered further for publication by eLife at this time. The reviewers raised three major issues regarding the clarity of the manuscript, the validity of the model, and the potential of the methodology to be used to generate biological insights in oocytes or additional cell systems. There were several concerns about the validity of the assumptions of the model, most notably the concern that as the coarse-grained model describes a substrate-enzyme binding reaction with a rate that depends only on the substrate concentration, this model would be valid only under conditions in which enzyme concentrations were orders of magnitude higher than substrate concentration. More broadly, the reviewers raised questions as to whether the assumptions in the model are valid in other systems and whether the methodology will be broadly applicable for the generation of novel biological insights. Given these significant concerns, we are returning the manuscript reviews to you so that they may guide you as you seek publication elsewhere. Should you wish to resubmit at a future date, we would be happy to reconsider a revised version that (1) more clearly justifies the validity of the approach and its assumptions and (2) provides an application of the new method to generate new biological insight.

Reviewer #1:

In this manuscript, the authors present a model to relate FLIM measurements to mitochondrial metabolic fluxes. Using mouse oocytes, which have little NADPH, the authors develop a coarse-grained model to infer mitochondrial NADH oxidation by exploiting NAD(P)H FLIM. Using this approach, the authors uncover regional variation in mitochondrial fluxes in mouse oocytes. The modeled mitochondrial flux shows a strong negative correlation with mitochondrial membrane potential and no correlation with mitochondrial content. While this is not the first paper to use NAD(P)H FLIM to show subcellular metabolic variability, this manuscript does present a model to connect NAD(P)H FLIM to mitochondrial redox cycles. Therefore, the major utility of the model lies in its ability to provide subcellular information about mitochondrial NAD(P)H oxidation. The authors provide a comprehensive and accessible discussion of the assumptions, caveats, and conclusions enabled by their modeling. At present, however, it is not clear to this reviewer how generalizable this method will prove beyond mouse oocytes. This concern stems from the potential difficulty in establishing key parameters of the model in other cell types in which assumptions safely made in mouse oocytes may not be appropriate.

To demonstrate the utility of their model, the authors should test key parameters in at least one additional cell type. In particular, the following issues should be addressed:

1. A key requirement of the model is the ability to determine the equilibrium NADH bound ratio. Here, the authors use low oxygen (or rotenone) to establish this parameter. Will this be feasible in other cell types, for example those with active NNT?

2. The authors note that the confounding signal from NADPH can be ignored in mouse oocytes, which have 40-fold higher NADH than NADPH. How generalizable is this? Will other mammalian cell types be amenable to this method?

3. The authors test the assumption that NADH signal originates in the mitochondria by comparing with mitotracker signal under control conditions. This should also be repeated for key conditions (e.g. low oxygen or oxamate treatment).

Reviewer #2:

In the manuscript "Coarse-grained model of mitochondrial metabolism enables subcellular flux inference from fluorescence lifetime imaging of NADH", the authors use fluorescence imaging to estimate NADH/NAD turnover flux and electron transfer rate in the mitochondria of mouse oocytes. Because of high spatial resolution of microscopy, the authors could also observe significant subcellular spatial gradient of oxidative flux in oocytes.

The fluorescence imaging and quantification of flux are generally solid and convincing, but there are issues that need to be addressed.

– In figure 1c, the author estimated two parameters τl and τs under different oxygen levels. They should be constant in all oxygen levels if this model is valid, but they vary a lot when oxygen level is below 10µM. However, the NADH concentration and bound fraction only vary a lot in this oxygen range. This should be addressed.

– The author used a mixture of LDH and NADH to prove the FLIM works in vitro. However, there are lots of different types of enzyme and complex in mitochondria that can bind NADH, and the author's model combines them together to do the calculations. Some justification of this is needed.

– In the spatial model, does variation of thickness of oocyte from center to periphery affect fluorescence levels? If yes, have author corrected this effect and how to correct?

– The nucleus will also cause heterogeneous distribution of mitochondria, which might also need to be considered in modeling spatial distribution.

Reviewer #3:

This paper describes an analysis of fluorescence lifetime imaging (FLIM) of NADH in mitochondria in intact mouse oocytes, using a mathematical model to interpret the fluorescence data to infer mitochondrial NADH redox fluxes. The authors measure FLIM data for varying oxygen concentrations and using several other perturbations to mitochondrial respiration, in order to infer consequential changes to key mitochondrial metabolic fluxes. One striking observation is of subcellular spatial gradients in the inferred metabolic flux across the oocytes.

The authors tackle an important issue in measurement and understanding mitochondrial function in intact cells. The analysis of the FLIM data is dependent on a mathematical model that the authors develop. The correctness and suitability of this model is not clear to me from the way it is described in the manuscript.

The analysis is based on a model, presented in Appendix 2, which considers 'course graining' of a 'detailed' NADH redox model. The latter considers N oxidases and M reductases acting on NADH and NAD+. The aim of the course graining approach is to reduce this model to an equivalent model with one effective oxidase and one effective reductase, and to calculate the effective binding and unbinding coefficients for this reduced model as functions of the binding and unbinding coefficients of the full model. This reduced model is then used to analyse the fluorescence lifetime imaging data, to infer mitochondrial redox fluxes, and to draw some conclusions on spatial gradients of mitochondrial function within the oocytes.

As the analysis and interpretation of the fluorescence lifetime imaging data depends closely on this model, it is necessary to (a) be convinced that the full model is an appropriate representation of the underlying system, and that (b) the course graining methodology is valid.

In relation to (a), the full model (Figure 2 in Appendix 2, but seemingly never presented as a system of mathematical equations), it is not clear why the authors have chosen this particular kinetic scheme, and there is seemingly no specific justification given for it. A simpler scheme would be (for example, for the ith oxidase)

NADHf + Oxi ⇌ Complex ⇌ NAD+f + Oxi

i.e. a standard reversible Michaelis-Menten scheme. It isn't clear why the authors have chosen to represent these reactions with two complexes, when a simpler scheme might suffice.

A more serious concern is in relation to (b), the validity of the course graining procedure that is subsequently outlined. The schema that is presented in Appendix 2 has the binding rates to be independent of free enzyme concentration. Thus, in Equation S6, for example, the binding rate for NADHf for the ith oxidase is koi,b∙[NADHf]. But as per the standard analysis of enzyme reactions (Michaelis Menten, etc), following from basic mass action principles, this should depend on the free enzyme concentration, and should instead be given by koi,b∙[NADHf]∙[Oxi] for the ith enzyme. No justification appears to be given as to why there is no dependence on the free enzyme concentration.

Unfortunately, a consequence of this is that the simple factorisation that allows equations S6-S9 to simplify into S10 and S11 is no longer possible. Essentially, by omitting the free enzyme concentration the authors end up considering a linear system which can be factored in the way they have presented, whereas the nonlinear system that is obtained when the free enzyme concentration is included does not allow this simple factorisation. It is this nonlinearity that generates the saturating behaviour in standard enzyme kinetics, for example.

Can the authors justify their linear model and omission of the free enzyme concentration? This does not appear to have been justified in the manuscript. One possibility that I can think of may be that the enzymes are all present in very high concentration, such that enzyme concentration is effectively constant. It is not clear that this is an appropriate regime. Alternatively, the authors should justify why the free enzyme concentration has been omitted in these equations. One way to demonstrate the validity of their approach would be through simulation, for example by selecting arbitrary parameters for a model with N and M oxidases and reductases and comparing full simulations of the nonlinear ODE system generated for this model with simulations of the reduced model derived from the course graining approach. As far as I could see there was no demonstration of the validity of the course grained model, however.

Otherwise, if the model is indeed incorrect, it is not clear what is the consequence of this will be on the subsequent data analysis (or indeed if the data can be analysed in this manner), given that Equation 1 in the main text and all subsequent analysis appear to follow directly from this assumption.

I hope that I am wrong, but if I am then I would strongly encourage the authors to provide further justification as to why their model and their course graining approach is correct and valid.

Reviewer #4:

Not every single cell is the same in terms of its metabolism. To study the causes of such cell-to-cell differences, we need microscopic tools to assess metabolic properties, such as metabolite levels and metabolic fluxes, on the single cell level or even beyond. While sensors exist to visualize certain metabolite levels, we still largely lack methods to assess metabolic fluxes in single cells. The work of Yang and Needleman presents a method that can assess -under certain assumptions- the flux through electron transport chain (ETC) in mitochondria of single mouse oocytes at quasi steady-states with subcellular resolution.

For their method, the authors use FLIM (fluorescence lifetime imaging microscopy) to determine the concentration of free and bound NADH in mitochondria, and these measurements are then used in a simple coarse-grained model to infer the flux through the ETC. This coarse-grained steady-state model describes the oxidation of NADH with one oxidase (resembling the ETC) and one NADH reductase (resembling all the 3 TCA cycle NADH dehydrogenases plus pyruvate dehydrogenase, but neglecting the FADH2-dependent succinate dehydrogenase) with only two free model parameters.

Strikingly, when fed with the FLIM data, this coarse-grained model could describe the outcomes of a number of perturbations, where the oxygen uptake rate (i.e. a proxy for the flux through the ETC) was independently measured with a different method. Applying the method, the authors also suggest that the ETC flux is higher in mitochondria that are rather located at the outside of the oocyte.

While FLIM measurements of bound and unbound NADH have been done before, the main strength of the paper is that it presents a method to infer metabolic activity in an oocyte, where the novelty resides on the development of the simple coarse-grained model and on showing that the model-based analysis of the FLIM data can allow to obtain quasi-steady-state ETC fluxes.

The main weakness of the paper is the following: Unfortunately, the work falls short on the application side. One would have wished that for a novel method like this, if it is indeed relevant, it should have been easy for the authors to add exciting application cases that would indeed generate novel biological insight.

While the main strength is the paper is the method (i.e. inference of ETC flux of model-based analysis of FLIM data), I feel that the description of the method, its assumptions etc falls short, which made assessment of the method and its potential limitations challenging. I feel that this is due to the fact that the writing of the manuscript is suboptimal. While the biochemistry is described/introduced on a very detailed textbook level, the methods, the measurements, the analyses of the measurement data in the result section and in the method section are described in a very short, condensed, and sometime convoluted, manner. As this is primarily meant to be a method paper, the authors need to do a better job in describing what they have done (i.e. model development, model assumptions, inference procedure, etc) in a clearer manner.

I felt that a strong point was that the two different versions of how the experimental data is used in the model, i.e. lifetime (tau) and bound ratio (β), leads to similarly inferred rox. However, due to the above criticized too short explanations, I could not tell whether this would be trivial or not. Also, the whole method boils down to this equation Jox = α * (β – βeq) * [NADHf], describing the full complexity of mitochondrial metabolism (TCA cycle, the electron transport chain, metabolite exchange between mitochondria and cytoplasm) with a single equation with only two free parameters (α, βeq). For this reviewer, also this part still remains somewhat elusive.

For publication of a new method in a journal such as eLife, I would expect that the manuscript also shows an application of the new method, which generates new biological insight, thereby demonstrating the power and value of the new method. With the measurements of the ETC flux in the spatially located mitochondria the authors start doing this, but unfortunately the manuscript does not develop this into anything interesting (i.e. unraveling of what could cause this gradient, where for instance one could do a dynamic addition of an inhibitor that would diffuse from the outside of the cell, etc). I think it is important to show a compelling case here.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "A coarse-grained NADH redox model enables inference of subcellular metabolic fluxes from fluorescence lifetime imaging" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Naama Barkai as the Senior Editor. Overall, all 3 reviewers were very positive about your revised manuscript. We would be pleased to accept a revised version that includes the textual modifications suggested by Reviewer #3.

Because we could not reach two of the initial reviewers, we added an additional reviewer at this stage. The following individuals involved in review of your submission have agreed to reveal their identity: Jason W. Locasale (Reviewer #2); Denis V Titov (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Please see the suggestions made by Reviewer #3 for clarifying points in the text. No additional experiments - only text revisions - are required.

Reviewer #1:

The authors have significantly improved the manuscript, which is much clearer than before. I think it is very interesting, although I cannot fully evaluate the strength of the assumptions. The authors take great care to explicitly address the major concerns raised by reviewers with regards to the assumptions of the coarse-graining model. Whether these clarified assumptions are valid is not obvious to me, as such modeling is outside of my expertise, but the concern appears to be addressed as far as I can tell. At least, it is clear in the text what assumptions the authors are making.

The finding that ETC flux is not regulated by substrate availability but rather by intrinsic ATP synthesis and proton flux is extremely interesting. While not a criticism of the manuscript, it is worth noting, though, that this result could have been achieved by OCR alone - as the authors show. Therefore, a major strength of this method is the ability to quantify ETC flux with subcellular resolution.

Reviewer #2:

Accept

Reviewer #3:

I was not one of the original reviewers of this manuscript. I have carefully read the manuscript, previous comments by 4 reviewers and authors response. I feel that authors addressed all of the comments raised during original review.

Below I provide comments based on my review of this manuscript, but I want to highlight that I feel that the manuscript is strong in current form and that model is interesting and well validated and that this model will provide interesting insight into activity of ETC in single cells or even subcellular compartment that is difficult to measure currently.

1) Interpretation of Figure 8 data/ homeostasis of ETC flux in MII oocytes. I agree with the authors that Figure 8 clearly demonstrates that various perturbations can lead to changes in redox status of cells without affect Jox/OCR and it is impressive validation of the model that not of these changes affect Jox validated by no effect on OCR. It feels to this reviewer that it is still entirely possible that textbook view that Jox/OCR is regulated by ATP demand is still correct here and it just happened that none of the perturbation that authors used were enough to significantly change ATP consumption in this system and instead all perturbations somehow affected substrate supply without changing demand. Since no measurements of ATP, ADP, AMP have been reported by authors, it is difficult to be sure that any of the perturbation actually affected ATP demand in a significant way although I agree that would have been my expectation. Perhaps, authors should consider adding this caveat to the text that it is possible that none of the perturbations changes ATP demand or if authors strongly believe this hypothesis is correct then showing that large changes in ATP, ADP, AMP are observed without change in Jox/OCR would strongly support this hypothesis.

2) Why does lifetime of free NADH change with low oxygen and with other treatments in other figures)? I can imagine how protein bound lifetime might change as the fractional contributions of proteins to which NADH binds might change with changes in [NADH] but I would have expected free NADH lifetime to stay the same. Perhaps authors should comment on this in the text to clarify this for readers and maybe provide examples of factors that can change free NADH lifetime.

3) Figure 1c. What are the confidence intervals for fitting-based estimates of lifetime and fraction bound of each sample? I could be wrong, but it seems to me that fitting of double exponential equation to decay data might produce redundant values for estimates of lifetimes and fraction bound. I think it would be useful if authors could add confidence intervals (e.g., using bootstrapping with randomly drawn points with substitution from each lifetime curve) that estimate the uncertainty of the fitting-based estimates to show that the fitting procedure used by authors produces non-redundant values of lifetimes and fraction bound. These estimates of uncertainty could also be propagated to Jox to provide a better estimate of Jox uncertainty compared to using one set of values from each FLIM trace that authors use currently if I understood correctly.
