# Peer review - Round 1

Editors:
- Marla B Feller, University of California, Berkeley United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.62091.sa1](https://doi.org/10.7554/eLife.62091.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Thank you for submitting your article "Synaptic inputs, but not action potentials, regulate motility of dendritic mitochondria in the developing visual cortex" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. The editors and reviewers have judged that your manuscript is of interest, but as described below additional experiments are required before it could be published.

We would like to draw your attention to changes in our revision policy in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option.

Overview of discussion between Editors and Reviewers:

This study explores the relationship between calcium signaling and mitochondrial motility in dendrites of developing visual cortex neurons. The manuscript provides interesting new insights into the regulation of mitochondrial movements in dendrites. Specifically it explains apparent previous discrepancies in studies on the role of activity in regulating mitochondrial motility by identifying differences between the impact of synaptic activity vs. action potential firing. The experiments appear carefully conducted, the findings are well illustrated, and communicated clearly in the text.

The reviewers agree that there are two interesting aspects of the study.

1) The in vivo demonstration that mitochondrial motility decreases in developing dendrites as activity increases and that this correlation holds for the effects of TTX on motility.

2) The in vitro finding that synaptic activity, rather than spikes, are what matters. We think if both these points were made convincingly, the impact of the study would be appropriate for eLife. However, the reviewers think these claims were not fully supported by the data.

The reviewers think the following needs to be done:

(a) cleaning up the analysis of the effects of local events on passing mitochondria to take into account of low overall motility and clarify effects at short intervals;

(b) showing that local calcium transients occur in vivo and have the same effect on mitochondrial motility as they do in vitro;

and

(c) locally activating synapses (e.g., glutamate uncaging or puffing) to show that this is indeed what drives mitochondrial arrests. To be clear -- (a) is required and either (b) or (c) should be sufficient.

Below is a consolidation of the original comments from individual reviewers that led to the above discussion and decision-- in some cases it may seem repetitive with the above, but it may be helpful to see how the reviewers struggled with some analysis as presented.

Summary:

In this study the authors explore the relationship between neural activity and mitochondrial motility in the dendrites of cortical neurons during development. The authors conduct simultaneous imaging of calcium and fluorescently tagged mitochondria motion both in vivo and in an organotypic slice preparation. They show that there is an increase in the frequency of global calcium transients with age and a reduction in motility. However, there is essentially no correlation between motility and spontaneous global calcium transients on a dendrite-by-dendrite level. Rather, they argue that mitochondria motility is influenced by synaptic activity. The data to support this are two-fold: first, mitochondria are more likely to stall near synapses if those synapses have been recently active; second, latrotoxin (which induces exocytosis) but not TTX leads to complete cessation of mitochondria movement. Finally, the authors construct a model to simulate how changes in synaptic activation impact motility making a few assumptions of underlying the arrest duration of mitochondria. The model suggests that given the observed local effects of synaptic activity on mitochondrial movements, the developmental decline in mitochondrial motility could be accounted for by the simultaneous increase in the density of synapses.

Essential revisions:

1. Given there appear to be very few motile mitochondria for any given dendrite, the authors need to be careful as to how they quantify their data. The example shown in Figure 1 appears to have perhaps 1 or 2 motile mitochondria our of 8-10. The quantification of the data is “percent of motile mitochondria”. As seen in Figure 1D, this corresponds to “bins” of percentile changes of 5-10%. Yet, the entire range used to establish the correlation in Figures 2A and 2B is 12%! Hence there is not much confidence that the resulting correlation is meaningful. There is even less confidence that the 1% change in percent observed in TTX (Figure 2F).

2. In figure 2 the authors quantify global Ca events and mitochondrial motility in dendrites in vivo over a range of postnatal days. As has been demonstrated by others (e.g. Faits et al., 2016), the authors see a progressive decrease in motility of mitochondria. They further demonstrate a negative correlation between global Ca events and mitochondria motility. The authors do not present whether they are able to detect spine-specific spontaneous events in-vivo and how spine-specific events change during this period of development. This seems important given the distinction made in vitro.

3. Figure 4 is quite critical to the study but several aspects were confusing. The authors argue that mitochondria are halted near a synapse after the synapse was active. This quantification depends on the length scale that means “near” and the time scale that means “after”. The authors need to clarify this quantification much more. Some questions:

– Figure 4E is based on 2 microns and 120 seconds compared to “before”. Does “before” mean less than 120 seconds or compared only to the time prior to spine activation?

– Figure 4F: the terms of the bootstrap analysis need to be clearly stated – is the hypothesis that seeing a reduction in motility >120 seconds is more than you would expect by chance if all the time points between 0 and 120 seconds are included?

– Figure 4G: I am quite confused here. Let’s take the lightest pink plot. Does this mean if you look at the interval 20 second after the synaptic activation that there are more mitochondria stopping prior to calcium transient than after?

Given all of these questions, the authors must justify 120 seconds as the most relevant time scale. Particularly if they get an opposite sign effect if you look at 20 seconds!

4. The primary manipulation in the paper is the application of LTX in the presence of TTX. This manipulation demonstrates that release of neurotransmitter in the absence of Aps can induce the stopping of mitochondria. However, it seemed unsatisfying that this manipulation was global in nature and not more local (e.g glutamate uncaging/ glutamate puffing/ stimulation of local axons) given that the authors make the distinction earlier between global and local calcium measurements. The authors discuss the potential mechanism by which a local (synaptically induced) calcium transient and a global (backpropagating AP induced) Ca transient could differentially regulate mitochondrial trafficking briefly I the discussion. Mechanistic findings of these differences would certainly elevate our understanding and the paper.

5. The latrotoxin effect is quite dramatic. Though it is true that latrotoxin induces exocytosis, my understanding is that latrotoxin does this causing a massive increase in intracellular calcium and influx of water. Hence latrotoxin may impact mitochondrial motility in a manner independent of synaptic release. Given that the TTX is also likely to impact synaptic release, this seems like the most likely explanation.

6. The authors argue synaptic activity not global cellular activation stops mitochondria. Hence TTX has a small effect and latrotoxin has a big one. But TTX also impact synaptic events as well as global calcium events. So why is there not a bigger impact of TTX on mitochondria? Do they authors argue that most of the synaptic activity is independent of evoked release? This point can be clarified.

7. In Figure 4, the authors present data on the effects of local calcium transients on mitochondrial motility. Panel G indicates that motility is enhanced shortly after the calcium transient and decreases after longer time intervals. This observation appears to approach or reach statistical significance. The authors should clarify whether this is a consistent observation and discuss what mechanisms may account for it.

8. It is not clear for many of the figures (e.g. Figure 2, Figure 3) what the size/ content of the dataset that is being analyzed. In particular, how many mitochondria are being tracked from how many dendrites from how many neurons from how many slices/animals. In figure 4 the text reads “In nine cells (P5 + 3‐7 DIV), we identified 157 spines of which 140 71 (45%) showed spontaneous synaptic calcium transients(376 transients).” This was very helpful to the reader to give an idea of the dataset and it would be helpful to include similar statements for other datasets. This is particularly important given that much of the data is presented as normalized data (e.g. percent moving mitochondria).

9. The authors develop a model that suggests that the local stopping of mitochondria in response to synaptic activity can in large part account for the age-dependent decline in mitochondrial mobility observed in vivo (~70%). The authors’ model suggests that this is only true if the mean arrest duration of mitochondria is around 5 minutes. The data in Figure 4I suggests that the mean arrest duration of mitochondria is about 1 min, but as the authors point out, this is likely an underestimate due to the fact that ~8/20 mitochondria remain at rest when their imaging session ended. Given the importance of this parameter in their model, longer imaging sessions would be necessary to determine mean arrest time more accurately. The data looks like in fact there may be a multimodal distribution of mitochondrial arrest time. As it stands, I don’t feel that the model provides much additional understanding.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Activity-dependent regulation of mitochondrial motility in developing cortical dendrites" for further consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing editors, and the evaluation has been overseen by Gary Westbrook as the Senior Editor.

The manuscript has been greatly improved and two the reviewers felt their concerns were adequately addressed. There remains a major issue regarding the quantification of the "%-motile" data brought up by Reviewer #1 that has not been satisfied. After discussion with all the reviewers it was deemed that this was something that needs to be addressed. We suggest that you consult with a statistician concerning this issue. We will not be able to make a final decision until that issue is adequately addressed.Reviewer #1:

Most of my concerns have been addressed in the revision. There is still one major concern remaining – and I have repeated it here.

The remaining concern was the first one I raised in first review and had to do with quantification of % motile mitochondria. Repeating what I said in this first review --

The example shown in Figure 1 appears to have perhaps 1 or 2 motile mitochondria out of 8-10. The quantification of the data is "percent of motile mitochondria". As seen in Figure 1D, this corresponds to "bins" of percentile changes of 5-10%. Yet, the entire range used to establish the correlation in Figures 2A and 2B is 12%! Hence there is not much confidence that the resulting correlation is meaningful. There is even less confidence that the 1% change in percent observed in TTX is meaningful (Figure 2F).

The only answer offered by authors is that this is the same method used in a previous study (MacAskill et al., 2009) but with shorter time windows. However, this is not a question of methods, this is a question of statistics and how reliable the effects are. As noted by authors in this manuscript, the longer time windows in the previous study led to a larger range of percent motile mitochondria, ranging from 0-50%. However this larger range is less susceptible to discretization errors, which is my concern here.

At a minimum, comparisons across conditions (Figure 2) should not be based on t-tests, which assume a normal distribution around a mean. With discretized date like this, the assumption of a normal distribution is incorrect – evidence of this can be seen in Figure 2B where the variance at P8 and P10 actually goes to zero.

An example of the implications of this is Figure 2F – their claim that TTX effects motility in vivo. They find the percent motile goes from 2% to 3% – again a finding based on individual measurements that are binned at >5%. Though they find this incredibly small effect significant using a t-test, this sort of small effect is susceptible to discretization errors.

The authors are requested to perhaps use longer time periods for their session so like the previous paper, it won't as susceptible to this error. At a minimum, the authors should perform a Fisher's exact test rather than a t-test to make statements regarding whether their effects on motility are significant.

Reviewer #2:

The authors have satisfactorily addressed my previous concerns.

Reviewer #3:

The authors have responded to my concerns regarding the clarity of the paper and analysis. They have addressed my concern regarding the lack of a local manipulation with new experiments (glutamate puffing). This led to a surprising finding that they discuss. Other concerns were addressed through more careful discussion in the manuscript. I feel the manuscript is suitable for publication.
