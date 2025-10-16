# Peer review - Round 1

Editors:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand

Reviewers:
- Ben Cooper, Mahidol Oxford Tropical Medicine Research Unit Thailand
- Elena Gómez-Díaz, Doñana Biological Station (EBD-CSIC) Spain
- Penelope Anne Lynch, University of Exeter Cornwall Campus United Kingdom

## Review text

DOI: [10.7554/eLife.40339.016](https://doi.org/10.7554/eLife.40339.016)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The impact of seasonal variations in Plasmodium falciparum malaria transmission on the surveillance of pfhrp2 gene deletions" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Ben Cooper as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Prabhat Jha as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Elena Gómez-Díaz (Reviewer #2); Penelope Anne Lynch (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This research represents a research advance which builds on a previous paper by the same group which considered the selection pressure exerted by the widespread use of rapid diagnostic tests for malaria in sub-Saharan Africa for deletions to the pfhrp2 gene, which can lead to false negative test results. Subsequent to the previous publication, the World Health Organization has produced guidance for the investigation of suspected false-negative diagnostic test results due to pfhrp2/3 deletions. However, this guidance says nothing about the recommended timing of such investigations. The current work uses an extension of the model-based analysis to show that seasonal variation in malaria transmission can lead to substantial biases in estimates of the prevalence of pfhrp2/3 deletions, leading to poor choices of rapid diagnostic test. The risk of this sampling bias is mapped by region, and optimum sampling intervals are proposed.

Essential revisions:

All reviewers thought that the work was important and conducted to a high standard and should be published if some essential revisions are made. These revisions are needed primarily to improve the clarity of the work and in some cases to extend the Discussion to consider other factors that might be important (see individual reviews below). Comments marked with a * below should be considered discretionary revisions. In particular, though non-essential, it was felt that an additional figure might help to clarify the relationship between monoclonal/multiclonal infections and pfhrp2 deletions prevalence and selection. An important part of these clarifications is provision of pseudo code for the revised model, just to document exactly how the updated DDEs shown in the manuscript are incorporated into the simulation model.

Reviewer #1:

The seems to be a useful research advance that addresses an important policy question using a model described in a previous eLife paper. The work is well-motivated and clearly described.

Reviewer #2:

This is an a research advance upon a previous study Watson et al., 2017.

In the previous article, authors modeled the potential for RDT-led diagnosis to drive selection of pfhrp2-deleted parasites. In the present work, authors extend the model so it now considers the impact of transmission intensity and seasonality on the prevalence of pfhrp2 gene deletions. They found that regions with low transmissibility and high seasonality are those with higher number of false negatives (higher prevalence of pfhrp2 deletions). They also show that this bias is stronger in young children.

The article is clearly written, the figures are very illustrative, and the new data support the conclusions. The new findings are significant. The data provided represents an important resource for the community.

- The extended analysis focus on seasonality and transmission intensity. I wonder about other possible causes of RDTs misdiagnosis. For example, the work seem to focus only on the clinical cases. What is the dynamics expected for pfhrp2 deletions in the asymptomatic? This is important because asymptomatic malaria significantly impacts transmission dynamics and asymptomatic infections show seasonality.

- The study model pfhrp2 deletions but no consideration is made about the effect of the type of treatment driving selection. There might be a temporal and spatial variability at this regards that has not been considered?

*- The link between transmission intensity and multiplicity of infections is clear. However, I find confusing the relationship between monoclonal/multiclonal infections and pfhrp2 deletions prevalence and selection. I think this should be elaborated further and possibly modeled?

- Previous studies indicated that PfHRP3 may play a role in the performance of PfHRP2-based RDTs. Do authors have data on pfhrp3? Apart of pfhrp2 deletions, could other sequence differences contribute to lower sensitivity of RDTs?

Reviewer #3:

This paper provides novel insights into an issue of practical public health importance. The results are interesting, and deserve to be disseminated and understood. In order to achieve this fully, the paper would benefit from greater clarity in some areas. Elements of the story which are perhaps viewed as self-evident by the authors may not be self-evident to readers, and are key to interpreting the paper and its results.

This paper adds seasonal variation to an individual-based model simulating prevalence of pfhpr2-del strains and false negative results in a population over time,. I have not attempted to check the original model, but the amendment shown in the current paper seems correct. Could the authors provide an updated version of the pseudo-code documentation reflecting the updates?

WHO guidelines recommend a transition from HPR2-based RDTs to alternatives when the prevalence of false-negatives due to pfhpr2 deletion exceeds 5%, and specify survey protocols to test for this. This paper focusses on potential biases in the survey results arising from variation due to effects of seasonality and transmission intensity. Since it is central to the paper's premise, a brief explanation of the WHO survey protocol is needed, with an explicit explanation of the links between the simulation outputs and the values measured in the protocol. I think the relevant values are all present in the paper, but their meaning and relationships could be more clearly explained.

Can the authors clarify the basis on which the 5% threshold value was selected by WHO? The bias discussed in the paper may have different implications depending on whether the key comparator is the underlying prevalence of pfhrp2/3 gene deletions or the annual average proportion of pfhrp2/3-del false negatives. Is there any potential to add some discussion about the implications of this study for the WHO threshold value, for example whether specific values could be specified for particular seasonality and transmission-intensity contexts?

The text regarding assumptions about selection and fitness (copied below) is confusing. False negative RDTs and consequent treatment choices reflected in the model will inherently exert selection, which seems to conflict with statements in the text.

'Additionally, there was no assumed fitness cost or selective advantage associated with pfhrp2 gene deletion, i.e. individuals who are only infected with parasites with pfhrp2 gene deletions are assumed to yield a false-negative RDT result. This decision allowed us to control for selection within our investigation. This ensures that the dynamics observed are only due to seasonal variation in transmission intensity, and not due to an increase in the frequency of pfhrp2 gene deletions due to a selective advantage by evading diagnosis. As a result, when reporting individuals who are pfhrp2-negative we assume that 25% of individuals who are only infected with pfhrp2-deleted parasites will still be pfhrp2-positive due to the cross reactivity of PfHRP3 epitopes causing a positive PfHRP2-based RDT result.'

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Impact of seasonal variations in Plasmodium falciparum malaria transmission on the surveillance of pfhrp2 gene deletions" for further consideration at eLife. Your revised article has been favorably evaluated by Prabhat Jha as the Senior Editor, a Reviewing Editor, and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

As you know, there was some confusion in this paper, as the original submission indicated that model did account for selection for pfhrp2 mutants, but the subsequent correspondence indicated that the model didn't.

While we understand that there is some value in considering the situation where the frequency of pfhrp2 deletions is not affected by selective forces (i.e. delayed treatment), clearly selective forces are likely to be acting in most settings and following consultation the consensus was that completely removing this real-world effect from the model was hard to justify. Therefore in addition to the analysis that has been done, the authors should add additional work where they do what they originally said they had done i.e. including a model where there is a selective advantage for pfhrp2 deletion changes/mutants as originally indicated.

The authors appear to be assuming that the intended meaning of the 5% threshold is the average proportion of HRP2 RDT results for patients infected with P. falciparum which are false negatives caused by pfhrp2/3 gene deletions, during a given year. The Discussion and conclusion then focus on differences between the prevalence of false negatives at specific timepoints during a year vs the average prevalence value over the year. It would hugely improve the clarity of the paper to state this assumption explicitly and early in the text. It is also necessary to demonstrate using information in the WHO documentation that this is in fact the intended definition of the WHO 5% threshold. Without unequivocal evidence that this is the precise meaning of the threshold value intended by the WHO, then the use of terms such as 'bias', 'overestimate', 'underestimate' etc. is unjustified throughout.

If it is not clear that the threshold is defined as an annual average, then the paper's message needs to change slightly. By indicating the extent to which the prevalence of false negatives can vary seasonally, even when the prevalence of gene deletions is constant, the results presented here indicate that a conscious choice about this aspect of the definition is very important. Should the threshold represent the acceptable maximum prevalence of false positives, or should it be the annual average. In either case, the results can inform strategies for applying the protocol in ways most likely to identify the required value.

Because of the extensive nature of the requested revisions and clarifications which cannot easily be summarized, more extensive comments from both reviewers are appended below. All substantive points should be addressed satisfactorily as we are unable to extend the review process beyond this next revision.

Reviewer #2:

The manuscript has improved and authors addressed most of my comments satisfactorily. I have however a few additional comments on the revised manuscript and rebuttal letter which I feel would require additional clarification.

- Exceptionally unhelpfully, the use of "false-negative" should be "positive" here. We carried out all our simulations with the assumption that individuals who are only infected with pfhrp2 gene deleted parasites will still be treated. As such, the gene deleted parasites behave exactly the same as the wild type parasites.

I am afraid I don't fully follow this reasoning. My understanding is that the motivation of the study was that pfhrp2 gene deleted parasites could be indeed misdiagnosed and so simulations should treat them as false negatives (Introduction, second paragraph). If simulations threat those as positive, how could the model effectively estimate the rate of misdiagnosis and the seasonality in such estimate? May I have missed something?

Besides, I don't think that the reviewers have actually addressed the real concern that came with their original consideration that false negative RTD pfhrp2 deleted parasites would allow them to control for selection.

- Related to the same issue above, and in response to my comment, authors replied:

"We do not include a selective advantage to pfhrp2 gene deletion (apologies again for the error mentioned at the beginning of our response) and so we would not expect there to see a temporal variability in the selection pressure. If we did consider this then there would definitely be a temporal element, with the increase in the absolute number of people who seek treatment (we assume a constant proportion of people with a malarial fever seek treatment) during periods of higher transmission causing an increase in the prevalence of the pfhrp2 gene deletion. It was because of this reason that we decided not to model selection, so that we could exclude this effect of selection and be more confident that the dynamics seen are due to the fluctuations in individuals being only infected with pfhrp2 deleted parasites."

The selective advantage comes with pfhrp2 gene deletion individuals being misdiagnosed and not getting treatment. If you consider those as positive you remove selection but this is not reflecting any more the reality of the situation.

- About the relationship between monoclonal/multiclonal infections and pfhrp2 deletions prevalence and selection.

I thank the authors about including a supplementary figure, but could it be possible to clarify further the relationships in the text?, saying that the relationship is unclear is not of much help.

- About my comment "The regions identified were areas with both a low prevalence of malaria and a high frequency of people seeking…" Were these the only factors?"

To which authors responded "These were the only factors we looked at within our modelling study".

I don't find this reply satisfactory. I know they modelled only those, but my comment was more a recommendation so it is acknowledged somewhere in the Introduction or the Discussion whether they could be other factors that have not been considered and have been shown or suggested to influence the misdiagnoses.

Reviewer #3:

The author's clarifications make sense and are helpful. However, my improved understanding of the authors' intentions and the results and conclusions presented in the paper has generated some additional questions and comments. I still feel that the paper would benefit from greater clarity.

My understanding is that the key values being considered are;

1) The proportion of HRP2 RDT results for patients infected with P. falciparum which are false negatives caused by pfhrp2/3 gene deletions at a given timepoint.

2) The average proportion of HRP2 RDT results for patients infected with P. falciparum which are false negatives caused by pfhrp2/3 gene deletions, during a given year.

3) The proportion of P. falciparum parasites in a given region which have pfhrp2/3 gene deletions.

4) The 5% threshold in the WHO guidelines.

It would be incredibly helpful if the authors could provide a precise definition for this, as the various wordings I have found so far in the WHO protocol and information note are open to interpretation regarding whether the 5% is intended to represent: a) The proportion of HRP2 RDT results for patients infected with P. falciparum which are false negatives caused by pfhrp2/3 gene deletions; or b) The proportion of P. falciparum parasites in a given region which have pfhrp2/3 gene deletions.

Part of a full definition for this value is the assumed timing. A quick review of the WHO documentation does not immediately yield any specific information about assumed timings, an absence which would be consistent with an assumption that the rate is effectively constant through a season, or might equally mean that the relevant value is that at the time of sampling.

In the paper, the authors appear to be assuming that the intended meaning of the 5% threshold is the average proportion of HRP2 RDT results for patients infected with P. falciparum which are false negatives caused by pfhrp2/3 gene deletions, during a given year (item 2 in the list above). The Discussion and conclusion then focus on differences between the prevalence of false negatives at specific timepoints during a year vs the average prevalence value over the year. It would hugely improve the clarity of the paper to state this assumption explicitly and early in the text. It is also necessary to demonstrate using information in the WHO documentation that this is in fact the intended definition of the WHO 5% threshold. Without unequivocal evidence that this is the precise meaning of the threshold value intended by the WHO, then the use of terms such as 'bias', 'overestimate', 'underestimate' etc. is unjustified throughout.

If it is not clear that the threshold is defined as an annual average, then the paper's message needs to change slightly. By indicating the extent to which the prevalence of false negatives can vary seasonally, even when the prevalence of gene deletions is constant, the results presented here indicate that a conscious choice about this aspect of the definition is very important. Should the threshold represent the acceptable maximum prevalence of false positives, or should it be the annual average. In either case, the results can inform strategies for applying the protocol in ways most likely to identify the required value.

There is also some confusion in the text between the prevalence of false positives results, and the prevalence of the gene deletion, with the text referring to change of RDT being triggered by an incorrect assessment of the prevalence of gene deletions (e.g. Introduction, fourth paragraph), suggesting that the authors may in fact be defining the threshold value as equal to value 3 in the list above.

These are key to the meaning and the implications of the work presented here, and clarity about what is being assumed or referred to is crucial to allow the text to tell its story clearly, and to make it easy to assess the consistency of that story. Confusing references to different prevalence values in the text should be reviewed and resolved wherever they arise throughout the text, including some specific instances detailed below.

Detailed comments:

Introduction, third and fourth paragraphs: In the third paragraph of the Introduction the authors give a definition of the WHO threshold value as being the prevalence of false negatives caused by pfhrp2/3 gene deletions. However, in the fourth paragraph of the Introduction they suggest that incorrect assessment of the prevalence of pfhrp2/3 gene deletions could drive the decision to switch to non HRP2 RDTs. Is there another mechanism in the WHO guideline in addition to the 5% false negatives threshold which would drive a change of policy based on gene deletion prevalence rather than false negative RTD prevalence?

'The protocol in this guidance details how to estimate the local prevalence of false-negative PfHRP2-based RDTs due to pfhrp2/3 gene deletions and recommends that a national change to non PfHRP2-based RDTs be made if the estimated prevalence is above 5%.'

'the timing of the 8-week interval chosen within a transmission season could lead to bias in the sampled prevalence of pfhrp2/3 gene deletions. An overestimation of the true prevalence of pfhrp2/3 gene deletions could result in a switch to a less sensitive RDT'

Results, first paragraph and similar elsewhere in text: 'In a moderate transmission setting, a clear seasonal pattern is predicted (Figure 2C), with sampling at the beginning of the transmission seasons resulting in significant overestimation of the true proportion of false negative RDTs..'

'true' is not adequately defined to be used here in this way. It might legitimately be assumed to mean the population prevalence of false-negative RDTs at the time of sampling. What is meant here, I think, is that sampling at the beginning of the transmission season is expected to give a value higher than the true average value for the year.

Introduction, last paragraph, Figure 4 description and title, Results, last paragraph.

Introduction, last paragraph and figure description indicate that the values used to generate Figure 4 are the gene deletion prevalences

Results, last paragraph and implication of contents of plot indicate that the plot is based on prevalences of false negative values.

Results, first and last paragraph and Discussion, first paragraph and similar elsewhere in text – 'biased' and 'unbiased' are a mathematical terms with specific meanings and it is not clear that those meanings are correctly applied here and elsewhere in the text. It would be better to replace them with other terms unless the mathematical meaning is genuinely indicated.

Discussion, first and second paragraphs. These paragraphs both begin by describing the research presented in the manuscript as relating to estimates of prevalence of pfhrp2 gene deletions. The remaining text all seems to actually describe the results regarding the prevalence of false positive HRP2 RDT results, but the first sentences mean that it all reads as discussion of the gene deletion prevalence.

'This research characterises the potential for surveillance in highly seasonal areas within sub-Saharan Africa to produce biased estimates of the prevalence of pfhrp2 gene deletions. These findings highlight the impact of both the seasonal timing and…'

'Our modelling predicted that there would be increased observation of pfhrp2 gene deletions after periods of lower transmission and within younger individuals…'

Discussion, first, third and fourth paragraphs. 'However, the true prevalence of parasites with a pfhrp2 gene deletion in each administrative region is fundamentally unknown, and as such, our results should not be interpreted as predictions of the bias in future sampled estimates of pfhrp2 deletion. They should instead be used to support surveillance efforts and to reinforce the need for longitudinal measures of pfhrp2 gene deletions conducted at the same point with a transmission season.'

Is this compatible with the database mentioned in the Discussion? 'To support surveillance efforts, we have published an online database detailing the optimum sampling interval as well as the sampling bias throughout the transmission season for each administrative region'

'The observed prevalence of pfhrp2 deletions is higher when monoclonal infections are more prevalent, with the highest prevalence observed when sampling at the start of the rainy season as individuals are less likely to already be infected. Similarly, the observed prevalence of pfhrp2 deletions is higher in younger individuals who have lower clinical immunity, as they are more likely to present with clinical symptoms after their first infection event.'

Should these two references be to prevalence of false positives rather than prevalence of pfhrp2 deletions?

Discussion, last paragraph. This seems to be simply repeating contents of first paragraph of Discussion?

Subsection “Characterising the impact of seasonal transmission intensities upon pfhrp2 deletion prevalence”, last paragraph. '…fitting the frequency of pfhrp2 gene deletions in each simulation such that the true prevalence of false-negative RDT results due to pfhrp2 deletions is equal to 5%.'

'.. percentage of intervals that did not include the true prevalence of 5% was calculated.'

'true' not adequately defined, should simply say '.. the average annual prevalence..' or similar.

Figure 1 legend. '..In I – L and M – P the proportion of clinical cases due to pfhrp2-negative parasites is shown for both the whole population and..'

Wording is confusing, does this mean cases infected only with pfhrp2-negative parasites?

'…the population allele frequency of pfhrp2 gene deletions, which was set equal to 6% at the beginning of each simulation..'

Is the reason for or significance of the 6% value given anywhere?

'…10 simulation realisations are shown in each graph, with the mean shown with the thicker line. Lastly, the 5% threshold for switching RDT provided by the WHO is shown with the black line in plots I – P…'

I think the means are shown by the black line, and the 5% by the dashed horizontal line?

Figure 3 legend. Should '..age and seasonality..' be '..age and transmission intensity..'?

Figure 4 legend, description and title. '..pfhrp2 deletion..' should be '..false-negative pfhrp2 RDTs?..'

Should also be revised as necessary to reflect assumed exact definition of threshold value.

pseudo codesecond line 048

'// Loop through every day in simulation and calculate the seasonal curve for that day

045 FOR day: = 1 TO t_max // t_max is total simulation time in days

046 theta[day]:= Fourier_average +first_cosine_term * cos(2*pi*day/365) +second_cosine_term * cos(2*2*pi*day/365) +third_cosine_term * cos(3*2*pi*day/365) +first_sine_term * sin(2*pi*day/365) +second_sine_term * sin(2*2*pi*day/365) +third_sine_term * sin(3*2*pi*day/365))

047 ENDFOR

// Loop through every day in simulation and normalise seasonal curve for that day

048 FOR day: = 1 TO t_max // t_max is total simulation time in days

048 theta[day]: = theta [day] / mean(theta [1 TO 365) // normalise theta with first 365 days of theta

049 IF ([day] < 0.001) // with only 1st 3 terms of Fourier used we need to check for <0

050 [day]: = 0.001

051 ENDIF

052 ENDFOR

I'm assuming this is just a problem with the pseudo code, not the actual code, but that should be checked and confirmed. It seems that in the normalisation loop, the sum of theta values by which θ(n) is divided will use the normalised rather than original values for all θ(<n).

Could the authors please review the pseudo code for consistency with the actual code?
