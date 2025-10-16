# Peer review - Round 1

Editors:
- Caroline Colijn, Simon Fraser University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.49206.sa1](https://doi.org/10.7554/eLife.49206.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The dynamics of resistance in response to antibiotic treatment is of central importance in understanding resistance emergence more broadly. This paper develops a data-driven model to describe the within-host dynamics of Enterobacteriaceae that produce extended-spectrum β-lactamase. Supported by the model, the authors compare different antibiotics' effects on resistance.

Decision letter after peer review:

Thank you for submitting your article "Quantifying antibiotic impact on within-patient dynamics of extended-spectrum β-lactamase resistance" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Amy Mathers (Reviewer #2); Lulla Opatowski (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This work asks what the dynamic consequences of antibiotic perturbations are to the human gut flora, and addresses this question with a novel mathematical model that is fit to data. The authors use the model to estimate the impact of antibiotic treatment on the abundance of resistance (through blaCTX-M) and on the duration of carriage of resistance. Overall, the manuscript represents a potentially important contribution to the field. However, there is some T data overlap in a previous study by the authors. and we have identified a few essential revisions to resolve this issue and that need to be addressed as well.

Essential revisions:

The reviewers brought up the previous publication, Meletiadis, J. et al., 2017, in which a good portion of the cases were reported, and where some of the same conclusions were reached.

The authors should clarify the novel contributions of this work in light of the previous manuscript. It seems that the key claimed results here are (1) variability, Figures 1, 2; (2) effect of treatment on relative resistance; (3) effect of treatment on abundance and (4) the model with fitting, and consequently the estimates re duration of carriage. Each has limitations.

Please set these results, with the novelty and limitations, in context.

The modelling is clearly new and I think it is important. In that direction, the clarity should be improved. I particularly noted the very long paragraph in subsection “Dynamic within-host model”, and the benefit that explaining the model and its assumptions (and limitations) for non-statisticians, non-modellers would likely bring.

Please clarify re interpretation of 16s, abundance as noted by reviewers.

Please improve Figures 1 and 2. While "hieroglyphics" may go a bit far, I agree that Figure 1 is visually striking but hard to see and interpret. Perhaps in Figure 1 you could group the time curves by similarity, or present an expanded view of some representative curves, with the full set in an appendix. Or something like that.

Reviewer #1:

The motivation for this study and its goals are certainly important and timely. The collateral effects of antibiotic treatment on the distribution of bacteria species and strains in the enteric flora (microbiome) of humans and the incidence of antibiotic resistance genes and resistance encoding plasmids are subjects of considerable importance, epidemiologically as well as clinically. In their Introduction, the authors do a fine job of presenting this and particularly so for the extended-spectrum β-lactamase (ESBL)-producing Enterobacteriaceae and the blaCTX family of resistance genes, that are the focus of their study.

This investigation certainly has the virtue of being extensive; fecal samples were taken sequentially from 133 hospitalized patients from three countries (Romania, Serbia and Italy) for a median of five samples from each patient. This virtue does have a downside; these patients were hospitalized for different reasons and treated orally of intravenously with 10 different antibiotics. The results presented suggest that some antibiotics are more likely than others to affect the distribution and abundance of these enteric bacteria and the blaCRX-M genes, their study is correlative rather than mechanistic. From the results presented, it's not clear how the different modes and purpose of treatment the within-patient dynamics ESBL resistance. From what they say in their Discussion, the authors are very much aware of this limitation of this study.

Although their observation some antibiotics are more likely than others to affect the enteric microbiome and the frequency of blaCRX-M genes could have epidemiological and clinical implication, they don't really consider these potential implications of their results. It's also not clear how this information can be used. Presumably the choice of antibiotics, mode and frequency of administration in these hospitalized patients is based on the nature of the infection and information about the susceptibility of the target bacteria to the drugs employed for treatment. While in an ideal world, consideration should to the collateral effects of treatment; we are far from that ideal world. This is particularly so for hospitalized patients. It would be of some interest to do an analogous study for the treatment of community-acquired infections (about 90% of antibiotic use in humans), where information about the collateral effects of treatment with different antibiotics may have broader and implications that could be implemented.

Reviewer #2:

This is an interesting and important piece of work demonstrating the correlation between certain antimicrobial exposure in patients and associated increase in abundance of blaCTX-M. The gene increase is then normalized to 16s abundance for overall internal QC for extraction efficiency and bacterial content. The work appears to be very well done and the methods and approach to analysis appear to support the conclusions of the authors. The figures are easy to interpret and additive to the manuscript (not sure if Figure 1 is critical but it is interesting to look at the variability across the data set and would favor keeping). Also the discussion includes a portion focused on relative biomass and bacterial presence in the gut of patients on antimicrobials but it is not clear they would be able to infer this information from the variability in swab collection and extraction efficiency. Would favor revising the discussion to address this issue.

One concern is the amount this manuscript overlaps with another previously published manuscript (Meletiadis, J. et al., 2017). The authors state in the Introduction section that they used a subset of the data but in reviewing the other manuscript it appears that there are 133 patients in this analysis and 122 from the other description. They also used very similar methodology by normalizing the blaCTX-M abundance with 16s. I think it would be helpful for the authors to further explain how this differs from prior work and is additive to the literature. The conclusions from that manuscript were almost identical as well. Would favor a re-write to address this existing work and contrast the submitted manuscript.

Reviewer #3:

Niehus and colleagues present an original study in which they investigate the impact of different antibiotics on ESBL resistance within-host in Enterobacteriaceae carriers. The data comes from 133 patients from Romania, Serbia and Italy and consists in longitudinal series of rectal swabs (with a median of 5 swabs per patient). Swabs were analysed in order to quantify the abundance of blaCTX-M and 16SrRNA. For both indicators, the within- and between-host variabilities, and the within-host dynamics are analysed using Bayesian state-space models. Parameters associated to the selection exerted by different classes of antibiotics on the dynamics of blaCTX-M, 16SrRNA and blaCTX-M/16SrRNA are estimated.

This is a very exciting and well written article. This is, to my knowledge, the first study attempting to analyse, using hypothesis-driven mechanistic models, the dynamics of within-host resistance genes and the impact of various classes of antibiotics. I believe that the study and results presented here represent a major contribution to the field.

– It would be good for the reader to detail and clarify how each indicator should be interpreted. My understanding is for example that a decrease in blaCTX-M/16SrRNA would more or less be interpreted as a decrease in resistance rate. However, it is not clear to me how important is the contribution of Enterobacteriaceae species to the global quantity of 16SrRNA.

– My main comment is related to the simulation study. It would be good to provide a validation of the model before running simulations, for example by doing out of fit assessment? Is that possible? Would you have enough power?

– It would be interesting to estimate whether the antibiotic classes have different delays of impact.

– I am not an expert but my understanding is that the aptitude to induce degradation of the flora may not be fully characterized by the "broad spectrum" characteristic. Other characteristics define whether the antibiotic destroys or not non-pathogenic (and anaerobic?) bacteria. It would be good to discuss more that aspect.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Quantifying antibiotic impact on within-patient dynamics of extended-spectrum β-lactamase resistance" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Wendy Garrett as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Antimicrobial resistance is recognised by the World Health Organization and others as one of the most pressing threats to global health. However, our understanding of the ecological processes that link antimicrobial use to the emergence and spread of resistance is limited. In particular (and surprisingly for such a fundamental question), a quantitative understanding of the within-host processes relating clinical antibiotic exposure to within-patient resistance abundance is lacking. For bacteria that colonize the human gut, such within-host processes are likely to play a major role in mediating the relationship between antimicrobial use and the prevalence of resistance in the wider population. This paper focuses on resistance in Enterobacteriaceae conferred by extended-spectrum β-lactamase (ESBL) production. Such ESBL-producing organisms are responsible for a high and increasing burden of disease globally. The authors aimed to determine the effects of typical antimicrobial exposures in hospitalized patients on the dynamics of resistance gene abundance and total bacterial load. The authors asked: if such effects exist, how do they vary between different treatment regimens, and what is the predicted impact of antibiotic exposure on persistence of patient colonization with ESBL-producing organisms?

Essential revisions:

The manuscript remains of high interest because of the conceptual innovation of this work related to the model.

However, reviewers still do not fully understand the dynamical model, which in our view was one of the key points of novelty of this work because it makes the link between mechanistic processes and the noisy observations. Accordingly, further revisions of this section should be completed before the paper can be accepted for publication.

It would be helpful to link the data to the notation so we know which symbols correspond to data. For clarity, even after doing this please note which are the hidden-state variables (in the dynamic model; it's listed in the observation/process noise model).

Technically, the notation a, b refers to a closed interval so infinity should not be listed in this form. We would suggest simply the phrase "improper uniform prior".

Equation 4 and text: it appears that you haven't "added them on a log scale" because the sum that you have computed goes into the mean of the normal distributions in Equation 4.

What does xt=1 = xt=1a0c1c2 have to do with any of the terms in (4) ? The text in remains inscrutable compared to the equations and notation. There is mention of the model "looping" through time points – how does this work? Please expand the text and be explicit about the likelihood at each stage, what the looping steps are, whether the terms are added to the mean or are multiplicative, and so on. Please define xi,j,g=ratio, xi,j,g=16S and all notation.

When you say that you "fitted the model with STAN" please give the posterior decomposition, and the likelihood. State which parameters are estimated. The notation of the model should be connected to Figure 4 and 5 where the model's inferences are shown.

Despite the response to review where you agree that it will be difficult to assess "abundance", you then include the following statement. It seems that the authors agree with the limitations around abundance in the response to review but then do not fully incorporate into the discussion. Please consider revising. Example: “Surprisingly, despite the relatively broad antibacterial spectrum of cefuroxime and ceftriaxone, there was no evidence that exposure to these antibiotics reduced 16S rRNA abundance (although we note that a "broad" spectrum is not defined in relation to the microbiota but to bacterial species of clinical importance).”
