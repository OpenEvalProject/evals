# Peer review - Round 1

Editors:
- Roberto Cabeza, Duke University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32696.sa1](https://doi.org/10.7554/eLife.32696.sa1)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Large-scale network integration in the human brain tracks temporal fluctuations in memory encoding performance" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Sabine Kastner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal her identity: Jessica Cohen (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you can read below, the reviewers had several positive comments about your manuscript. They think that your study is interesting, novel, and important. They also praised your control analyses and the MVPA analysis.

At the same time, they had several concerns that must be addressed in the revision. Instead of repeating the reviewers' comments, I will highlight few issues in which the reviewers converged and/or I find particularly important.

1) Both reviewer 1 and 2 commented about the use of the Power et al. atlas. Reviewer 1 thinks the use of the Power et al. nomenclature is excessive and asks you to justify better the choice of this atlas. Reviewer 2 suggests adding the hippocampus to this atlas, so you can confirm the hippocampus-occipital effect you found using the Kim's ROIs.

2) Reviewer 1 noted your excessive use of reverse inference, which I also found excessive in the Discussion section. Perhaps instead of speculating about the contributions of brain regions you did not specifically investigate, you could use the Discussion section to focus on several issues noted by the reviewers.

3) Reviewer 1 commented that the 30-sec time window is not appropriate given the fast dynamics of memory encoding. I agree with this point. I also agree with reviewer 2 that, because of the long time window, the difference in memory between high and low memory states is small (comment #5). You have to report the average number of HH and LL/Miss trials in the two states. It would seem there were about 6 trials and 3 fixations per window, which means that with a mean of HH trials around 50%, high and low memory states could differ in just one HH. I suggest that you redo the analyses with a shorter time-window and using a parametric analysis with tertiles or quartiles as suggested by reviewer 2.

4) Reviewer 1 commented that your point that DMN activity is associated with subsequent forgetting is not true for the hippocampus, whose activity is assumed to be part of the DMN but shows subsequent memory effects. You need to discuss this issue, which has been previously investigated (e.g., Huijbers et al., 2011). Personally, what I found surprising is that you link the DMN to subsequent forgetting in the Introduction, but you then find higher DMN inter-subnetwork integration for high than low memory states and do not mention this apparent inconsistency in the Discussion. I suggest you report standard event-related analyses to confirm you are getting the standard subsequent forgetting effects in the DMN, particularly ventral parietal and posterior cingulate in your study. If so, you would have an interesting dissociation between activity and connectivity which could enhance the study.

5) Reviewer 1 notes that your conclusion that high encoding state is characterized by long- rather than short-range functional connectivity is not supported by any statistical analysis. Independently, reviewer 3 suggested a method for addressing this issue: use Euclidean distance of edges. I think you should add this analysis and ideally report a 2 (range: long vs. short) x 2 (memory state: high vs. low) interaction.

6) In addition to these points, the reviewers had several other comments you should address, such as using other measures of sub-network interactions (see Wig, 2017), investigate the connectivity of SFE regions, do additional analysis to control for potential motion confounds, and consider potential.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Large-scale network integration in the human brain tracks temporal fluctuations in memory encoding performance" for further consideration at eLife. Your revised article has been favorably evaluated by Sabine Kastner (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

Reviewer 1:

1) Add an ANOVA to the last paragraph of the subsection “FC patterns among memory-encoding-related regions”.

2) Qualify the use of "short" in "short time windows (~36 s)".

3) Emphasize the "breaking" of resting state functional connectivity pattern during high encoding (changes in inter-subnetwork connectivity as opposed to FC increases).

4) Do not lump the hippocampus in with the DMN (focus on specific regions).

5) Clarify that subnetwork integration contributes to encoding (not the "core" roles of networks).

Reviewer 2:

1) Report only the 32P+scrubbing results.

2) Do not use "moment-to-moment".

3) Discuss studies using shorter time-scales, such as Sadaghiani et al. (2015).

4) Look at DMN subnetworks (e.g., Fornito et al., 2012) or community-detection algorithms to determine if the DMN is separated into multiple subnetworks during memory.

5) In first paragraph of the subsection “Dynamic reconfiguration of a large-scale functional brain network”, but not the conclusion, says that there is a general increase in long-range and decrease in short-range connections distributed across many networks, rather than a uniform increase/decrease in FC across the entire network.

6) Correct "Cohen & D'Esposito, 2016".

Reviewer 3:

1) Provide additional data explaining why the supplemental analysis show modularity was greater for high than low encoding states when movement is properly controlled.

2) Re-run the models without redundant regressors.

3) Add missing statistical tests.

4) Why weren't the SVMs run with the other variables?

Full comments of the reviewers:

Reviewer #1:

1) The stats starting in the last paragraph of the subsection “FC patterns among memory-encoding-related regions” require an ANOVA. Specifically, when comparing hippocampal and occipital connectivity for SME vs. SFE, separate t-tests are not appropriate (Nieuwenhuis et al., 2011).

2) "By analyzing time-varying FC within short time windows (~36 s)".

As indicated in the past review, "short" here is really incorrect. Single neuron studies show SME effects on the order of hundreds of milliseconds (Viskontas et al., 2006). Such effects are also present at the network level during retrieval in the local field potential on the scale of hundreds of milliseconds (Watrous et al., 2013). Thus, the authors really need to clarify in more detail in the Discussion that "short" here really refers to a state rather than specific processing related to memory. I suggest adding one or two sentences in the Discussion and mentioning these papers briefly.

3) "These findings suggest a systematic reconfiguration of the large-scale functional brain network related to incidental encoding performance, rather than a uniform increase/decrease in FC across the entire network."

I still think the authors need to be clearer that their findings also suggest "breaking" of resting state related functional connectivity patterns during high vs. low encoding states. Thus, the findings would also seem to support the idea that inter-subnetwork connectivity is important to these memory states rather than just increases in FC within them. There is some mention of this in the Discussion, but I was surprised not to see this point emphasized in more detail.

4) "(e.g., the hippocampus and other regions in the DMN)"

The authors should be careful here. The Power network does not include the hippocampus and different authors seem to lump the hippocampus in with the DMN while others do not. I suggest removing the statements about the DMN here and focusing on those specific regions. The authors may also consider an influential paper by Rugg and Vilberg that makes a much better case for memory specific brain regions than the resting state literature (Rugg and Vilberg, 2013).

5) "In our case, the results from these two metrics convergently suggested the core roles of the subcortical, default-mode, and visual systems in incidental encoding of visual stimuli."

Again, I think the authors should be careful here. They also showed integration across subnetworks was important to successful encoding. This doesn't suggest the "core" roles of these subnetworks themselves but rather their integration with each other, at least in the context of the paradigm investigated here.

Reviewer #2:

1) I appreciate the inclusion of the section of the Results "Addressing possible concerns about motion confounds". While acknowledging potential confounds is important, given the improved methods to deal with motion beyond the 6 motion parameters plus WM/CSF as you report in your main analyses (8P), I cannot think of a reason to not simply report the 32P+scrubbing results. As you acknowledge, the results are quite similar across the two methods. However, the differences across the methods may be related to motion, especially given your findings that FD is related to behavior, and that it is related to global efficiency without the more rigorous nuisance regression. These pieces of evidence all point to likely spurious results when you do not aggressively account for motion and other artifacts. Thus, I think you should remove all results using the 8P method and only report results using the 32P+scrubbing method.

2) At the beginning of the Discussion, you write: "We demonstrated dynamic reconfiguration of a large-scale functional brain network associated with moment-to-moment fluctuations in encoding performance." I would rephrase that, since moment-to-moment implies volume-to-volume (i.e., on the order of your TR) and/or differences on the resolution of individual trials; by using 36s, non-overlapping windows, this is longer than "moment-to-moment".

3) Related to the timing, most of the literature you cite having done similar analyses (arousal, sustained performance across blocks of a perception task or working memory/Stroop task), include tasks or states that are thought to vary on longer timescales, while your Introduction is about subsequent memory, which is categorized on a trial-by-trial basis. While I find the results you show averaging across trials convincing and an important contribution to the literature, more of a discussion about the shorter-scale changes in your case would be relevant. As it is, you briefly mention the shorter time-scale in the results but do not bring it up again. As an example in the literature, the Sadaghiani et al. (2015) paper that you reference looks at a small number of volumes before each detected or missed stimulus and does so on a trial-by-trial basis. A method like that seems appropriate for truly looking at subsequent memory, and as such should be discussed.

4) With regard to your discussion of the involvement of the DMN, it is helpful that you now point out that some regions within the DMN are also related to memory. Why don't you look at sub-DMN networks, which has been done in other studies looking at memory network dynamics in the past (i.e., Fornito et al., 2012; and others)? Or, in the very least, suggest using community detection algorithms to determine whether the DMN is more accurately separated into multiple subnetworks during memory?

5) In the first paragraph of the Discussion subsection “Dynamic reconfiguration of a large-scale functional brain network”, I appreciate the increased specificity in your explanation. However, it selects only two examples (there were significant increases within more networks than just the DMN, for example) thus it misrepresents the results. Additionally, the specific examples in contrast to the summary of distance effects is confusing – the distance effects appear to be across the whole-brain and not related to individual networks, whereas you initiate the paragraph giving examples only of a small subset of individual networks. It seems as though a conclusion more in line with the results is that there is a general increase in long-range and decrease in short-range connections distributed across many networks, rather than a uniform increase/decrease in FC across the entire network.

6) Finally, as a small comment, this paper is cited incorrectly in the in-text citations: "Cohen and Esposito, 2016" is incorrect; it should be "Cohen and D'Esposito, 2016". I see it cited about 4-5 times, so it should be fixed each time.

Reviewer #3:

1) My first concern centers on the results following more appropriate strategies for dealing with movement, which is known to impact time-course correlations. I appreciate the effort that was put towards minimizing movement-related confounds. A large proportion of the analyses do not survive correction for multiple comparison corrections. More critically however, a supplemental analysis indicates that modularity is actually increased during high encoding states relative to low encoding states when movement is properly controlled. This is in large conflict with the remaining analyses, and is incompatible with the conclusions of the paper. As the paper is framed around segregation and integration, the fact that the closest measure to segregation exhibits an opposite pattern to that which is discussed is problematic. The authors discuss this point a little and offer a scenario where modularity and efficiency can exhibit opposing patterns (subsection “The effects of denoising methods”, last paragraph), but I'm not convinced that the disconnect between their measures has been reconciled. I believe additional work needs to be done to explore this discrepancy, possibly centering in on what parts of the network are driving the effect, as readers interested in the network side of things will question the basis for the conclusions.

2) For both the GLM and time-course analysis (the latter of which is used for all subsequent connectivity/graph comparisons), it appears all trial-types have been modeled explicitly (high-hit, low-hit, miss, fixation; subsection “Trial-related activation analysis”). As a result, I think the models contain redundant regressors which can impact estimation of the regression coefficients and residuals. This should be corrected.

3) A number of necessary statistical tests are missing to allow comparisons across states/measures. Specifically, for examining SME/SFE by state, the analysis of within subnetwork connectivity should reveal an interaction, as that is what is being implied and interpreted. It is currently presented as a series of pairwise comparisons (subsections “FC patterns among memory-encoding-related regions” and “FC patterns across large-scale brain networks”). Likewise, for local/global efficiency/PC vs. high/low encoding (subsection “Graph analysis on large-scale brain network”), a comparable ANOVA model is required to confirm the existence of interactions.

4) Why weren't SVMs run with the other variables? Is there a reason why the authors only report the results of PC, subnetwork local-e, and whole-matrix FC patterns (subsection “Multivariate pattern classification using graph metrics as features”)?
