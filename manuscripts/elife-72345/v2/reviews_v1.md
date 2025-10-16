# Peer review - Round 1

Editors:
- Claire Wyart, Institut du Cerveau et la Moelle épinière, Hôpital Pitié-Salpêtrière, Sorbonne Universités, UPMC Univ Paris 06, Inserm, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72345.sa0](https://doi.org/10.7554/eLife.72345.sa0)

This work presents a conceptual advance on our understanding of the habenula in vertebrate species, by revealing interesting functions to specific cell types within this region of the brain.


---

# Peer review - Round 1

Editors:
- Claire Wyart, Institut du Cerveau et la Moelle épinière, Hôpital Pitié-Salpêtrière, Sorbonne Universités, UPMC Univ Paris 06, Inserm, CNRS France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72345.sa1](https://doi.org/10.7554/eLife.72345.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Specialized neurons in the right habenula mediate response to aversive olfactory cues" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Marianne Bronner as the Senior Editor. The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The three reviewers have appreciated the novelty and originality of the study, but note that improved visualization, quantifications and statistical analyses will be necessary to fully support the conclusions of the manuscript. Without performing these quantifications and statistical tests for all figures as detailed below, the magnitude and significance of reported effects are not clear, nor do they take into account the variability of the measures and the dependence of some of the measures.

1. Anatomy (Figure 1):

The authors should verify the specificity of the novel transgenic lines generated in the study to target lratd2a+ neurons in the right dHb (some left dHb expression is seen in Figure 1C-E). In addition, improving the quantification of c-fos and lratd2a overlap is necessary.

2. Calcium imaging and response to chemical stimuli (Figure 2):

The effects of the aversive chemical stimuli on the calcium activity of the lratd2a+ cells in the dorsal habenula are not clear in the traces presented nor quantified for all cells in all fish recorded. As a matter of fact, the traces of single examples show responses to water alone and not a very clear effect of the olfactory cues. The statistics are lacking to compare the response to water, cadaverine and chondroitin sulfate. The authors should determine whether the olfactory stimulus used induced a larger response than water in the same cells. They should assess the variability across fish, and the reliability of the effects. We advise to use linear mixed models which are suited to take into account the variability of cells within the same fish, as well as the effect of clutch or day of the experiment. In order to to take into account the effect of time and pairing within the same cell that receives the water stimuli before the olfactory ones, we recommend using a linear mixed model with a fixed effect of time (measuring the average or max DFF before, during and after the chemical stimulation) and treatment (olfactory cue added), pairing values within the same cell and same fish.

3. Behavior (Figures 3 and 4):

The effects of genetic manipulations on the response to cadaverine and chondroitin sulfate should be quantified and compared across genotypes using a proper statistical tests. In the submitted manuscript, the authors only quantified an effect of the drug within each group using t-tests using only the last point before the drug was applied, instead of comparing between the groups the effects of different genotypes on the preference index at all time points (before and after the application of the olfactory cue). This is an issue for both figures, note that in Figure 4 the preference index during baseline might differ between the wild type and mutant group. The authors should use a two-way repeated measures analysis of variance (ANOVA), or Kruskal-Wallis test for non-parametric data, to assess differences between treatment groups over time for validation studies, and test the effect of the drug over time within each group and between conditions before and after. By doing so, the authors will determine whether there is an effect of time, whether there is an effect of genotype and if there is an effect of time, measure the effect of an interaction. Note that if the authors opt for the ANOVA, they should perform post hoc comparison tests using either the Tukey method (commonly used to make pairwise comparisons) by correcting for multiple testing or t-tests with Bonferroni correction for multiple comparison. By doing so, the authors will determine whether there is an effect of time, whether there is an effect of genotype and measure the effect of a possible interaction.

Reviewer #1 (Recommendations for the authors):

Figure 1: Anatomy

To show that lratd2a+ neurons receive inputs from the olfactory bulb, the authors rely on gross low scale overlap of YFP+ axons on the soma of mApple-CAAX in the triple transgenic line lratd2a:QF2; QUAS:mApple-CAAX; lhx2a:YFP,

– A: First thing, add a quantification of (a) the number of neurons that are expressing lratd2a in the wild type fish at 7, 14, 21dpf and adult stage and (b) the number of neurons labeled in the lratd2a:QF2 transgenic line and the left and right side as it is central to the study – in the C panel, there seems to be expression of the transgene obtained by KI in the lratd2a locus (lratd2a:QF2)c601 in the left side.

– Next, add histological examinations or higher fluorescent images for panels D-D".

– Finally, can you specify if the overlap has been observed at the level of single planes or projections as it should be to suggest direct connectivity? If so, add a quantification to illustrate the overlap based on single planes from optical sections obtained on confocal with high mag and resolution and close up.

Figure 2: Calcium Imaging

– A: in order to understand whether the response of lratd2a+ neurons is specific to aversive cues: can you show the response to (a) water (as illustrated in B), (b) one other aversive cue as well as (c) one non aversive cues?

– A: for 14 dpf and response to chondroitin sulfate, please add the number of neurons missing.

– A: for 21 dpf and response to chondroitin sulfate, how come there are only 16 neurons measured instead of ~>35 ? Does it mean that the line is variegated and numbers can vary from 15 to 40 in the right habenula?

– B: since spontaneous activity is large and we cannot conclude for single examples, panels need to show the variability across cells and not only single trace : (a) use mean and ste to show the intrinsic variability of the response across cells and (b) quantify the response by calculating the peak and subtracting the baseline averaged over a similar time window before stimulation.

– C: the response to cadaverine measured with cfos is not clearly overlapping with expression of lratd2a: the authors should perform double fluorescent in situ labeling to demonstrate the overlap at the cellular level.

Figure 3: Behavior of adult zebrafish expressing botulinum toxin in a subset of neurons in the right dorsal habenula.

– A-E: the authors should validate that the intersectional genetics combining a KI line, the QF2/QUAS and Cre under the scl5a7a promoter is effective to target the lratd2a neurons only and which proportion of them. On these images, it appears that the KI line has expression on the left Habenula as well.

– G-J: The effect of the expression of the botulinum toxin is not clear at all (for the preference index: T-test a single time points on a subset of them can be misleading) statistics need to be improved : if the data is quantified and plotted every minute, we would expect to compare the conditions before baseline and establish that there is no difference in preference index before addition of cadaverine, and that a difference is observed after the addition and quantify for how long.

For the alarm substance, the data is not represented the same as for cadaverine: in the single measure of before/after, there is no difference across genotypes in speed, onset time of the fast swim, or time between fast swimming and freezing. But would there be a difference for cadaverine using the same single measure of before/after ? Probably not.

The statistics and choice of parameters needs to be sorted out and represented fully and fairly with consistency across compounds and figures.

Figure 4: Behavior of left-isomerized adult zebrafish.

– Expression of lratd2a is affected in the dorsal right and ventral right and left habenula so the mutant does not reveal only the role of lratd2a+ neurons in the dorsal right locus.

– Same issue here for the behavior: the pre-condition appears possibly different for the homozygous mutant and control sibling. The authors should test whether there are any difference of preference index in the two groups before drug application, and after drug application.

– Why are again different parameters plotted in H-G for the alarm substance compared to cadaverine? In addition instead of time onset and interval between fast and freeze, duration in the top of the tank is quantified. This choice looks arbitrary and all parameters should be chosen and kept the same for comparing the effects of cadaverine and alarm substance.

Reviewer #2 (Recommendations for the authors):

1. If calcium imaging experiments were to be repeated, water and odorant cues should be alternated so a direct comparison can be made for individual neurons. Also, both sides of the habenula could be simultaneously imaged, with lratd2a neurons labeled with another (e.g. RFP) marker, to allow for comparison between left and right habenular responses.

2. Can c-fos experiments be performed on the lratd2a transgenic background in adults to facilitate quantification?

3. While not necessary for this paper, chemogenetic approaches (e.g. TRPV1 from Prober lab) could be useful to activate the population

Reviewer #3 (Recommendations for the authors):

The authors of this work describe how cholinergic neurons expressing the lratd2a gene of the right dHb increase their activity to aversive odorant guiding aversive behaviors. The design of the study is very elegant, especially exciting is the combination of genetic tools that allow to label, as well as manipulate synaptic function. The authors present elegantly their data, and my impression is that this work deserves publication. The author may want to consider the following points:

1. The concepts of aversion and avoidance are confusing. Avoidance implies a form of learning (see reviews from J LeDoux) after an individual learns to anticipate an upcoming aversive stimulus. If I correctly interpreted the authors use a on-line reading of escape/aversive behaviour after inclusion of cadaverine. This should be probably better defined throughout the text.

2. At one point in the results the authors make use of a genetic approach allowing to control synaptic function with Botulinun neurotoxin. They state that "Axons labeled by BoTxBLC-GFP terminated at the vIPN.…. suggesting that botulinum neurotoxin inhibits synaptic transmission within this restricted region of the vIPN". I understand the technology is used in published data, yet it would be elegant to show along with the behavioural results an assessment of collapsed synaptic function.

3. The authors use a labeling strategy that allows claiming that the cholinergic neurons innervate a precise area of the IPN, supporting previous data in literature. In their data set the authors however study the functional responses to cadaverine only in somata of these neurons. It would be extremely relevat in my opinion to show that calcium transients are also detectable in the Cholinergic axons in the IPN. This would corroborate the functional integration of aversive signal within this neuronal circuit, and not only within the right habenula.

4. The authors may want to consider referring to the following reviews when citing habenula work in rats, mice, and humans in the context of physiology and disease: Hailan Hu et al., 2020; Lecca et al., 2014; Proulx et al., 2014.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Specialized neurons in the right habenula mediate response to aversive olfactory cues" for further consideration by eLife. Your revised article has been reviewed by 2 peer reviewers and the evaluation has been overseen by Marianne Bronner as the Senior Editor, and a Reviewing Editor.

The authors show an interesting role of a subpopulation of habenular neurons in the avoidance response to aversive olfactory cues. We thank the authors for improving the manuscript, particularly for repeating the calcium imaging experiments and for improving the data presentation. There are however some remaining issues that need to be addressed, as outlined below.

Essential revisions:

1) Overall the behavioral differences to cadaverine shown in Figure 3G (Cre- vs Cre+) are relatively mild, especially as the aversion indices are significantly different from baseline in both Cre- and Cre+ condition (Figure 3—figure supplement 2B). Given that this is a key experiment in the paper, a discussion regarding whether this is a limitation of the existing tools (e.g. insufficient neurons silenced) or a reflection of underlying biology (e.g. redundancy in circuits for avoidance, different circuits controlling duration vs magnitude of aversion) would be beneficial.

2) Presentation of Figure 2c-d can be improved further – the same neurons presumably are being imaged "before" and "after", however the way the data is currently plotted makes it look like they are independent neurons.

3) It is counterintuitive that a negative aversion index means stronger aversion (perhaps call it a preference index instead, or flip the signs so more positive = more aversive).

4) In the aversion assay (3G, 4E, 5F): can the authors clarify if some form of multiple comparisons correction was done in calculating the p-values at each time bin?

5) The authors have performed ANOVA on the aversion indices shown in the supplementary figures, and report a significant effect of odor and odor x group interaction. Is there a significant effect of group alone? there is no explicit mention of the aversion index in the main text, and no interpretation in the figure legends. For clarity, the authors should elaborate how the statistical results from this 2nd analysis method ties in with / complements the statistical methods used in the main figures.

Reviewer #2 (Recommendations for the authors):

I thank the authors for improving on the manuscript, particularly for repeating the calcium imaging experiments and for improving the data presentation.

While significant effort has been put into improving the statistics, I have some additional questions about the analyses performed and their interpretation. Ultimately I will defer to the other reviewers regarding whether they are satisfied with the current methods.

For the main figures, I was expecting a two-way ANOVA to be performed for the time course data in the aversion assay (3G, 4E, 5F) to compare main effects of group and time and group x time interactions. I understand the authors are using a different methodology here (signed rank test) which has also been applied in other papers – however, can I clarify if some form of multiple comparisons correction was done in calculating the p-values at each time bin?

The authors have performed ANOVA on the aversion indices shown in the supplementary figures, and report a significant effect of odor and odor x group interaction. I might have missed something, but is there a significant effect of group alone? I also do not see any explicit mention of the aversion index in the main text, and no interpretation in the figure legends. For clarity, perhaps the authors could elaborate how the statistical results from this 2nd analysis method ties in with / complements the statistical methods used in the main figures?

Overall the behavioral differences to cadaverine shown in Figure 3G (Cre- vs Cre+) are relatively mild, and the aversion indices are significantly different from baseline in both Cre- and Cre+ condition (Figure 3—figure supplement 2B). The data is what it is, but given that this is a key experiment in the paper, a discussion regarding whether this is a limitation of the existing tools (e.g. insufficient neurons silenced) or a reflection of underlying biology (e.g. redundancy in circuits for avoidance, different circuits controlling duration vs magnitude of aversion) could be refreshing.

Reviewer #3 (Recommendations for the authors):

All my specific points were addressed by the authors. The complementary experiments and the modification provided in the text improved the paper and it is in my view suitable for publication.
