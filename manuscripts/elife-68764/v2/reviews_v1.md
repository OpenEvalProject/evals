# Peer review - Round 1

Editors:
- Gwenan M Knight, London School of Hygiene and Tropical Medicine United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68764.sa1](https://doi.org/10.7554/eLife.68764.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper provides a mathematical modelling framework for a stepwise incorporation of ecological complexity up to the effects of host microbiome on the spread of antibiotic-resistance. This provides a key first step in our understanding of the heterogeneous impact of the host microbiome on the spread of resistance, as demonstrated by the author's application of the model to four key pathogens.

Decision letter after peer review:

Thank you for submitting your article "Microbiome-pathogen interactions drive epidemiological dynamics of antibiotic resistance: modelling insights for infection control" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Esther van Kleef (Reviewer #1); Erik S Wright (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Summary:

The reviewers agreed that the approach is thoughtful, and the analysis performed is well complemented by simulations using relevant parameters in healthcare settings in hospitals. The big problem with this area, which is stressed by the authors, is the lack of information to support parameter choice. Despite being stressed, it was often not completely clear how and why parameters were chosen. Further clarity is required to support publication of this work which does offer a rational framework for linking the epidemiology and the microbiome, with an important hypothesis for antibiotic resistance.

Essential revisions:

The main revisions required are

– A restructuring of the methods to provide greater clarity of model structures and justification of parameter choices (is there no data? why was this chosen if so?). The driving force behind this should be the reproducibility of the work and the exploration of the results based on the parameter choices.

– A rewriting of the introduction and discussion to include more context of prior modelling work as well as to provide justification for the focus of the work

– In line with (1), all reviewers were in agreement that this work needs a clear single model description: a formal description of the model framework in one place. This could be in the supplementary, but it needs to be a well referenced place.

1) In general, the model the authors use is highly parameterized. There is a worry about circular reasoning when modelling. Parameters are derived from observations, then a model is constructed to recapitulate this observation. Then similar observations are used to show the model's validity. How did the authors ensure this type of bias was not incorporated into their modelling? This can become a bigger issue with more highly parameterized models, and that is why simpler models are preferable. Another approach is to use cross-validation, although we are not sure how that would work here.

Abstract

2) The Abstract is vague and somewhat convoluted as written. It did not do the best job of selling the paper and does not convey any specific information.

Introduction

3) The authors need to tailor this to their specific question: where is the knowledge gap? We recommend that the authors think carefully about the statements they are making and consider revising the Introduction to include a more thorough analysis of prior modelling work, which is largely absent from the Introduction.

4) The study focuses on four particular pathogens, however, no motivation of why they are chosen is provided, nor the relevance of their analysis in a more general overview is discussed. The authors could expand on how their results could be extended to other contexts/species in which the role of microbiome on resistance is also relevant. This could also be included in the discussion.

5) The authors conclude that disruption of the microbiome on an individual level (due to antibiotics) can result in selection for AMR on a population level. In a way, the work is, at least in part, a model-based implementation of the theoretical perspective of Lipsitch and Samore 2002 EID doi: 10.3201/eid0804.010312 (which describes how antibiotic effects on an individual, within-host level, can affect population level transmission dynamics). Could the comparison to Lipsitch and Samore and the novelty of the improved data-driven approach (although still limited) be further discussed?

6) Antibiotic stewardship is treated a single entity, whereas in reality there are countless types of stewardship interventions and a concomitant variety of outcomes. Comparing the model's results directly to an analysis of previous stewardship interventions and attempting to show alignment does not make sense to me. How were these stewardship interventions reflective of the model? Why would we expect agreement or disagreement a priori? The fact that there was agreement with the model was somewhat concerning given the complexity of many stewardship interventions.

Methods

7) In attempting to replicate this study, it became intractably difficult to recreate the ODEs because the equations and variables are interspersed throughout the main text and supplementary appendix. For example, in Figure 1e the authors mention differences in resistance levels (γ) and not transmission rate (λ, related to β as in Equation (3)), the value of which could not be found anywhere in the text. Similarly, where is patient demography (Δ) incorporated into equations 3 or 4? There are certainly answers to these questions, but it would have been helpful to have the model more clearly presented in a central location. Finding the parameters and making sense of them was extremely challenging, if not infeasible. Therefore, we were unable to replicate the results to any extent.

8) It is unclear how the authors arrived at their parameter values throughout the manuscript. For example, colonization resistance (epsilon) as it is formulated is not compelling, and where did the value of this parameter come from? It is listed in Table S5 as being drawn from a Cauchy distribution. Why? Where did these numbers come from? Some of the parameters seem justified by literature, but the rest are perhaps debatable. This might be inevitable with a complex model, but the authors should minimally provide a robustness analysis to each of their less-supported parameter choices. What would be the outcome if the sampled distributions had been wider (e.g., if the true value had been different by an order of magnitude)?

9) The inclusion of the 'r' parameter, allowing for partial resistance in the resistant strain, is interesting (and innovative for modelling frameworks to our knowledge). Nonetheless, it is not clear why the authors use a baseline of r = 0.8 to illustrate the trade-off between antibiotic induced clearance and selection for Cr (Figure 1F), whereas in figure 2, the authors use r=0.4, i.e. higher levels of sensitivity in Cr. I suppose with a lower r, strain coexistence is more likely, and thus higher likelihood of Horizontal Gene Transfer (HGT) (?), but it would be, for consistency and comparison of the different within-host dynamics, more transparent to use the same baseline parameter values, unless the authors can provide a good reason why different values of r are assumed at baseline between Figure 1 and Figure 2B?

10) The model presented in Eq. (1) needs a better introduction. Is this a new model or based on other models previously studied? This is explained later in the text citing references (30) and (31), but we recommend to introduce them earlier. It would be also good to point the reader earlier in the main text to the first sections of the supplement for a better understanding of the model assumptions and parameters employed.

11) Also, should the parameters be more consistently labelled across frameworks? For example, we recommend writing λ(N,C), or something similar, in all the equations to explicitly state it depends on these parameters. The way it is written gives the impression that λ is a constant parameter.

12) The r vs resistance rate (Cr/Cr+Cs) caused some confusion. This as a resistance rate of Cr = 0.8 but an r = 0.4 could actually mean that 0.8*0.4 = 0.08 of pathogens carried are fully resistant against the antibiotic, while this is 0.64 when r=0.8. Can the same baseline values for r be used in Figure 1 and Figure 2 or the differences justified?

13) Furthermore, in figure 1F: this is representing a one strain model. Is the Ce+Cd strain similar to the Cr? Can this be clarified?

14) In line with this. In Figure S3, R0 seems to represent the R0 of Cr. However, for Figure 1H and 1I, how should R0 be interpreted respectively? And for Figure S2? Please clarify how similar Cr (Figure 1H) and the one strain modelled (which could be similar to the Cr strain of Figure 1H) for figure 1I are

15) Figure 2A, the minimum resistance rate is 0.35 (see legend, and this appeared the case when no antibiotic induced clearance nor antibiotic induced microbiome disruption). This seems rather high. In particular as in Figure 2B, minimum levels of less than 0.1 are shown. Could the authors explain where this discrepancy is coming from and to what extend these high baseline resistance rates are representative?

16) For parameterisation of the models for the different pathogens, estimates from literature, notably existing modelling studies are chosen. However, these estimates, at least for C. difficile and MRSA, are coming from models that don't incorporate endogenous acquisition explicitly (for the Enterobacterieacia, model estimates from Gurieva are used, which do use a modelling framework incorporating an exo- and endogenous acquisition). Therefore, the acquisition rates may be overestimated for these gram-positives, in particular for C. diff the endogenous acquisition, which is listed as the main acquisition route (pp 14 line 330).

This may affect the estimated intervention effectiveness (in particular for antibiotic stewardship (less effective) and contact precautions (more effective)) under assumptions of the microbiome model. Could the authors use more realistic estimates (not sure models with explicit exo- and endogenous acquisition exist for MRSA and C. diff), or at least, reflect on how different values of α and β affect the model results?

17) It would be helpful to explicitly say how the simulations were performed, i.e., mention that the ODEs where integrated. My first impression was that the authors performed stochastic simulations using the processes illustrated in panels A, B, C from Figure 1. This is probably an issue that only mathematical modellers would have, but could the authors please add this clarification.

Discussion

18) The model is described by a set of differential equations. This means the model ignores stochasticity of the population size dynamics of each strain. The authors could expand a bit more on the assumptions of the model and why fluctuations are ignored.

19) Also, spatial structure is particularly important when taking into account interactions between microbiome and pathogens, but it is also neglected in the model. It would be useful if the authors could discuss this as well.

20) The results shown often focus on steady-state quantities (such as colonisation prevalence), but the temporal evolution of the model is not discussed. It would be interesting if the authors could investigate the timescale of the different interactions taken into account, and how relevant they may be in the healthcare settings they investigate. Is the temporal evolution of the model any relevant for their conclusions?

21) Can the authors please add examples of the hypothetical microbiome recovery interventions they have in mind? Are the authors thinking of things like faecal transplantation? Please add, also to provide more practical interpretation of the work.

Reviewer #1:

The authors use a theoretical dynamic transmission modelling framework, incorporating both between and within-host dynamics of antimicrobial resistant (AMR) pathogens, to stress the importance of the microbiome in the transmission dynamics of bacterial species. The work considered five different colonisation models, comprising different variations of 'traditional' epidemiological models, which, according to the authors, often do not include within-host microbiome-pathogen interactions, and add such interactions. With regards to the latter, three different within-host microbiome-pathogen interactions, as well as horizontal gene transfer are considered, and their effect on population transmission as well as interventions, evaluated.

The authors have done an extensive amount of work, and have done a great job in documenting all the model assumptions, data used and methods employed. Also, visualisations and illustrations are nice and informative.

However, the main difficulty with incorporating within-host dynamics of AMR pathogens in a human-to-human transmission modelling framework is the lack of data to inform key parameters. The authors stress this limitation is also part of their work. The authors emphasise that they aimed to show in theory the importance of microbiome-pathogen interactions, and have conducted an expert elicitation to partly inform parameters representing these dynamics.

The authors conclude that disruption of the microbiome on an individual level (due to antibiotics) can result in selection for AMR on a population level. In a way, the work is, at least in part, a model-based implementation of the theoretical perspective of Lipsitch and Samore 2002 EID doi: 10.3201/eid0804.010312 (which similar to here, describes how antibiotic effects on an individual, within-host level, can affect population level transmission dynamics). Therefore, I am somewhere inclined to think, are the main points made by the authors new? As this work here does, similar to this earlier work, not provide a data-driven approach (although tries to some extend). On the other hand, the work does, in contrast to Lipsitch and Samore, provide a framework for how to model these interactions, and illustrate to some extend which parameter values require what data, as well as which dynamics are most likely at play for which pathogens. Moreover, what is new, is that the authors try to illustrate how such interactions may affect the effectiveness of interventions, which is an interesting and, to the best of my knowledge, a novel component. My comments are largely requests for clarification.

Reviewer #2:

Here the authors tackle the important challenge of incorporating the microbiome into a traditional susceptible-colonized transmission model. The microbiome acts as a third party in infections, with roles in supplying or suppressing antibiotic resistance. The authors found that microbiome interventions hold the promise of avoiding antibiotic resistance dissemination. This theoretical work encourages continued research into how the microbiome could be used to mitigate antibiotic resistance. However, I am skeptical of the translatability of the model's predictions to real infections. The model is heavily parameterized, without clear reasoning for some parameter choices. The work's greatest contribution, in my opinion, is that it offers a rational framework for how the microbiome could be incorporated into epidemiology, and provides an intriguing hypothesis that the microbiome could play a substantial role in combating antibiotic resistance.

I would like to say the authors clearly did a good job of conceptualizing infections and resistance dissemination. This was a substantial body of work and the manuscript was interesting to read. My biggest concern is that some of the results intuitively reflect parameters of the model, suggesting they might be artifacts of the approach rather than independent results.

Reviewer #3:

This manuscript by Smith et al. proposes a novel mathematical framework that contributes to the understanding of the role of microbiome on the resistance colonisation of bacterial pathogen populations exposed to antibiotics. The model proposed incorporates microbiome competition and takes into account dysbiosis effects on the population dynamics. Extended versions of this model that incorporates strain-microbiome competition and horizontal gene transfer contributions are also presented. The model is simple to understand and takes into account important considerations in healthcare settings usually ignored in the literature. The simulations performed use parameters of four pathogens obtained carefully from a panel of experts. The fact they used these parameters makes the implications of their analysis quite relevant in clinical infections. Different assumptions on the interactions of each of the pathogens are incorporated in the model, and different public health interventions are analysed. The study performed is quite complete and supports the authors objectives. Their work demonstrate how relevant is the accounting for microbiome interactions for the understanding of antibiotics incidence on antibiotic resistance. This is particularly relevant for future work on mathematical modelling of resistance.

Even though the work presented is well supported by the analysis performed, there are certain aspects regarding the model that need to expanded. In particular:

1) The study focuses on four particular pathogens, however, no motivation of why they are chosen is provided, nor the relevance of their analysis in a more general overview is discussed. The authors could expand on how their results could be extended to other contexts/species in which the role of microbiome on resistance is also relevant.

2) The model is described by a set of differential equations. This means the model ignores stochasticity of the population size dynamics of each strain. The authors could expand a bit more on the assumptions of the model and why fluctuations are ignored. Also, spatial structure is particularly important when taking into account interactions between microbiome and pathogens, but it is also neglected in the model. It would be useful if the authors could discuss this as well.

3) The results shown often focus on steady-state quantities (such as colonisation prevalence), but the temporal evolution of the model is not discussed. It would be interesting if the authors could investigate the timescale of the different interactions taken into account, and how relevant they may be in the healthcare settings they investigate. Is the temporal evolution of the model any relevant for their conclusions?
