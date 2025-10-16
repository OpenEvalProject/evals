# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science , Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.06559.016](https://doi.org/10.7554/eLife.06559.016)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors' note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for choosing to send your work entitled “Limits on information transduction through regulation of signaling dynamics” for consideration at eLife. Your full submission has been evaluated by Detlef Weigel (Senior editor), a Reviewing editor and two peer reviewers. We are potentially very interested in the work—provided that your premises hold up—,but because it is eLife policy to only invite revision when it is clear that required experiments can be done in a short time frame, we are declining the work for now.

The reviewers were overall positive in the sense that it was agreed on all that the approach is interesting and that the results are potentially important, but the reviewers were concerned that you did not address the (likely) possibility of loss of information between input and MSN dynamics. If a large fraction of information is lost already at this point, this could, unfortunately, invalidate your claims.

Reviewer 2 suggests how this can be measured experimentally, and further specify a criterion to when this loss can be ignored (and when it cannot). We will be very interested in considering again a manuscript that includes such experiments. Since we are uncertain whether the results would indeed verify your model, we are declining the work for now, but we are leaving the door open for a re-submission, provided the new experimental data will be supportive of your model.

Reviewer #1:

The paper from Hansen et al. addresses a key open question in signal transduction on limits the ability of gene promoters to accurately to decode signaling dynamics. Overall the paper presents interesting results that I would like to see published in eLife. I do have a major concern about input noise that I am worried could invalidate many of the major results and therefore must be addressed. Furthermore, I found the writing of the paper to have many unnecessary overstatements and over simplistic interpretation that need to be corrected through a major revision of the text. I discuss two key concerns related to overstatements and over simplistic interpretation below. I made two suggestions that are constructive, but not essential. The first is for an additional analysis that I think could improve the paper and is easy to do and therefore I strongly recommend it will be performed. The second require additional experiment and while I think it would improve the paper substantially but might be outside the scope of this work and I do not see them as essential as long as the statements made by the authors are appropriately toned down.

Quantifying noise in inputs:

The system the authors analyze has three components: microfluidics manipulation => MSN2 translocation => gene expression. They analyze the mutual information between microfluidics input class and gene expression. Therefore they make an implicit assumption that the information transmission between microfluidics class and the patterns of MSN-2 is “noise free” and that all the information loss is in the decoding MSN2=>YFP. However, in their 2013 MSB paper, the authors showed non-negligible variability in MSN-2-mCherry localization within their microfluidics setup. Furthermore, other factors could contribute to this such as the variation in MSN2-mCherry between cells. There are two ways to address this issue. The best way will be to repeat the experiments when measuring both MSN-2-mCherry localization and gene expression in the same cells and to calculate the MI between all steps in the pathway similar to Uda et al. 2013. However, this might require substantial new experiments that are potentially beyond the scope of this work. The second best way is to just show the mutual information between the inputs and MSN-2 dynamics (in absolute units to address MSN2-mCherry concentration variability issues). If this value is close to 3 (log2(8)) than the assumption that the input noise is negligible is justified is reasonable, otherwise the information loss could be in the “signaling” or the response . They should have at least some of the required for this in their MSB 2013 paper. If there is substantial information loss between microfluidics and MSN2 response then I must recommend that the paper be rejected and more experiment done to carefully analyze loss at different steps along the artificial “pathway”.

Statements that need to be revised:

Real upper bound limits on dynamics?

The claim that this paper shows a limit on decoding of dynamics is overstated. The real physiological dynamics of MSN-2 are much more complex than simple amplitude and frequency as shown by Nan and O'Shea, Nat Struct Mol Biol, 2012. It is very likely that the SIP18 and HXK1 are tuned to the real physiological dynamics and not to artificial AM and FM signals. In fact the authors actually show in Figure 2CD that these promoters are not optimized for these simple modes! The authors should restrict their claims to the information transduction through AM and FM signaling. This needs to be revised throughout the paper, Title, Abstract, main text etc.

Number of distinguishable states interpretation.

In this paper the authors constantly interpret their results as the number of distinguishable states. While this simplistic interpretation is tempting, I find it to be misleading for reasons explained nicely in Bowsher et al. 2014 which the authors cite. Mutual information should be interpreted as the increase in actionable information the cells has. Even a value of 0.77 bit could allow distinguishing between three states with some small associated inference error (see Bowsher 2014 Figure 1 and discussion in Box 2). I found section 2.4 in Supplementary file 2 that was supposed to address this issue to be very lacking. The paper should be revised completely to address this point including removal of Figure 5 and the many statements that argue that cells are limited to decoding identity and not intensity.

The use of information theory analysis is a great tool to analyze noise in signal transduction networks. This is a complicated tool and needs to be interpreted with care. However, as a community there was substantial disservice to this approach by using the over-simplistic interpretation of bits as number of distinguishable states. This was done in previous works by others and resulted in unnecessary resentment to information theory approaches. While I understand that it is a bit more challenging to write a paper that uses the more complex and accurate interpretation of the bit value, it is essential that we do so.

Constructive suggestions:

1) Compare analysis from Figure 3 to Figure 4.

It would be interesting to see in Figure 4 additional bars that show the mutual information done on the CFP/YFP cells from Figure 3. I believe that an analysis of the joint response of I(CFP, YFP; input) where CFP and YFP should show higher mutual information than a simple diploid YFP cell and basically similar level to the intrinsic mutual information calculated by the authors. This will provide validation to the analysis shown in Figure 3 and will allow better comparison of the results of the diploid.

2) Analyze the mutant promoters from Figure 2 in respect to physiological inputs.

Experiments that could be very helpful in general in addressing some of the issues mentioned above are the calculation of mutual information on physiological responses and not just manipulation of the dynamics. Specifically, it would be great to see if the mutants from Figure 2 also increase the mutual information from physiological response? I suspect that they will not and this will provide a relatively easy way to show that information is really encoded and decoded in the complex pattern of MSN-2 dynamics that goes beyond AM and FM.

Reviewer #2:

In this manuscript, Hansen and O'Shea reported the information theory-based analysis of the Msn2 signal transduction system. By controlling Msn2-mCherry nuclear localization dynamics and measuring its downstream target promoters, the authors revealed that the extent of information transduction for a single target promoter depends on the dynamics of Msn2 (AM or FM) as well as the number of STRE sites on the promoter. Additionally, the authors showed that integration of multiple target promoters enhances information transduction. Overall, I really like the information-theoretical analysis of signal transduction. While the conclusions presented are not overly exciting, i.e. there are limits on information processing through Msn2 dynamics, the experiments and analysis presented in this work opens up a new and interesting way of understanding single-cell signaling dynamics in general.

Major comments:

1) Cellular signal transduction is composed two steps: encoding step where (chemical) inputs are encoded into intracellular representation such as Msn2 dynamics, and decoding step where Msn2 dynamics are then decoded into target expression. In this manuscript, the authors focused on the decoding step, i.e., from Msn2 dynamics to promoter output. In all the analysis, the authors have assumed that Msn2 dynamics always follows the input chemical signal in every cell and thus the input TF signal equates the external chemical waveforms. However, I feel this assumption could present a fundamental problem in the analysis since it is hard to imagine that every cell in the population has the same Msn2 dynamics under a defined chemical waveform. More specifically, the distribution of responses (YFP level) could likely arise from the heterogeneous Msn2 dynamics among a population. Therefore, I feel that uncoupling the heterogeneity of Msn2 dynamics seems necessary for understanding how Msn2 dynamics contribute to the extent of information transduction.

2) Following the point above, the observed difference in signal transmission capacity between AM and FM Msn2 input may likely due to the difference in the degree of heterogeneity of Msn2 dynamics. For example, Msn2 may not follow the FM chemical signal as faithfully as the AM chemical signal. Thus, Msn2 dynamics could be more heterogeneous among cells in FM condition than in AM condition, leading to a more faithful signal transmission for AM. One might need to compare the variability in Msn2 response between AM and FM in order to study the role of Msn2 dynamics in the extent of information transmission in these conditions.

3) It occurred to me that the extent of information transduction positively correlates with the dynamic range of promoter response (Figure 2). In other words, by simply looking at the top rows (i.e., dose response curves) of each figure panel in Figure 2, I can immediately tell which condition transmits the most information (i.e., mut B AM). Is there any underlying principle that results in such a correlation? This correlation suggests that the dynamic range of the measurement may somehow affect the calculation of mutual information. A potential way to test if this is the case is to characterize the mutual information of the same condition under different lamp power or camera gain settings.

4) Regarding the calculation of the mutual information, maximum YFP level was used. The authors made the argument that final protein level is a biologically relevant quantity, which I agreed. In section 2.5 of Supplementary file 2, the authors made arguments about why other quantities are less desirable. I think the authors may want to make the argument more quantitatively. It could be that maximum YFP is the least noisy quantity and thus most suited for calculating mutual information. Such argument can be supported by comparing the CV of possible quantities, such as rate of YFP production, max YFP level, YFP level at a chosen time, etc..

5) I am not sure if the authors performed control experiments (in this or previous papers) to show that all the YFP expression (from promoters studied) comes from Msn2 alone (i.e., no other regulators involved). In other words, deletion of Msn2 abolishes the promoter expression under 1-NM-PP1.

[Editors' note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for choosing to send your work entitled “Limits on information transduction through regulation of signaling dynamics” for consideration at eLife. Your article and your letter of appeal have been considered by the original reviewers of the manuscript, and there are still some issues that need to be resolved before we can accept a revised paper.

Specifically, the appeal letter now includes the new experiment suggested by the reviewers, in which the information loss between the input and MSN2 dynamics is measured. As the reviewers originally worried, this information loss is quite substantial. This is a bit worrisome, especially as this value is inconsistent with lower loss inferred from the instrinsic/extrinsic analysis (Figure 3). Another issue is that this loss was measured only for the AM signal, and not from the FM signal. This may call for a major rethinking of how to interpret the results in the paper, and in this context, the reviewers suggested the following:

1) Change some of the interpretation of their data and present the paper with a careful analysis of the information loss due to intrinsic and extrinsic noise sources. This way, the fact that there is substantial loss between chemical input and MSN-dynamics is not a problem anymore, rather an interesting result. Between that and the comparison of AM/FM and the different mutants with increased dynamic range, there should be enough there for an interesting paper. The inconsistencies of the two methods would need to be addressed of course.

2) Quantify more directly the information transmission capacity between MSN2 dynamics and MSN2 promoter by measuring in the same cell MSN2 the dynamics of localization in the nucleus and the resulting promoter reporter. Since mutual information is a symmetric quantity, one could bin the promoter response into 8 or 16 bins. Than calculate the mutual information between the scalar MSN2 promoter response and the distribution of multivariate dynamics responses in each bin. This could be done by pooling all the chemical input data together and use an approach such as described e.g. in Selimkhanov et al. 2014 to calculate mutual information between scalar input and dynamic response. Perhaps the data in Figure 2-figure supplement 2 is sufficient, or if not, additional experiments are required.
