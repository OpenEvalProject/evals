# Peer review - Round 1

Editors:
- Helen E Scharfman, Nathan Kline Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97270.sa0](https://doi.org/10.7554/eLife.97270.sa0)

The study shows that activity of dentate gyrus mossy cells encode information from sharp wave-ripple complexes (SWRs) from the adjacent CA3 region. The study used difficult methods such as recording from multiple mossy cells simultaneously, as well as deep learning, which is impressive. The findings are fundamental in significance because they show a relationship between mossy cells and sharp wave ripples that has not been appreciated before, and the strength of evidence is compelling.


---

# Peer review - Round 1

Editors:
- Helen E Scharfman, Nathan Kline Institute United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.97270.sa1](https://doi.org/10.7554/eLife.97270.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Distributed encoding of hippocampal information in mossy cells" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions

1) Address the conceptual questions of Reviewers, especially Reviewer 1.

2) Clarify the deep learning approach as noted by all Reviewers.

3) Consider the statistical questions and revise as appropriate as noted by Reviewer 3.

Reviewer #1 (Recommendations for the authors):

Detailed additional concerns.

A ref is needed for CA3 neurons send input to MCs. I would suggest PMID: 7884451; PMID: 9157312 Note CA3 also sends input to hilar and GCL interneurons. For that I would cite PMID: 8008190, PMID 7473243, PMID: 8300905, PMID: 2358523.

Line 62

"there is no direct axonal projection from CA3 pyramidal cells to DG granule cells Fujise and Kosaka, 1999"

This is not likely to be true. Li et al. (PMID above) showed CA3 axons in the GCL and IML. However, I do not believe synapses were proven. Still, it is highly suggestive. Buckmaster showed similar findings in primate. PMID: 11135261

Line 63

"An estimated 15,000 MCs reside in the rat hippocampal formation, whereas approximately 300,000 and 2,450,000 CA3 pyramidal and granule cells exist, respectively"

I am not sure these numbers are correct. As a start, see PMID: 17765743, PMID: 17475251 Perhaps the authors are referring to a particular species and if so that should be discussed.. Finally, estimating GC numbers is very difficult because they overlap even in thin sections. So this needs to be considered carefully. See PMID: 29311853, PMID: 1793176, PMID: 3292009

Since it is not clear what the numbers are, it might be useful to show a range, and implement the deep learning with several possible values. If the results are the same that would make the results more convincing.

Line 66. Same caution needs to be made here

Line 103

I think the authors mean cells were excluded if capacitance was <45pF (please explain the reason) and they were included if they had spines and thorns.

Refs are needed that these are characteristics of MCs.

Line 109

Consider excluding cells with such instability that they were not held >1 min.

How were others designated healthy?

Line 465

Exposing mice to an enriched environment means what?

Why was this done? What were the effects? Was there a control?

Line 479

Why was -40 a cut off? That seems very depolarized and unhealthy.

How were MCs distinguished from CA3 or GCs? What about slow spiking hilar interneurons?

What were the brief inward currents exactly?

Line 480

What was the tungsten electrode exactly? What part of CA1 was recorded? Why? To record SW? If SW were recorded in CA1, the layer should be consistent. Was it checked?

Exactly how was DiI used?

Why were SW recorded in CA3 in vitro and CA1 in vivo?

Was the site in CA3 in vitro consistent across slices? How was it positioned so it was consistent?

Why is the term SW used, not SWR?

Line 503

'The detected events were scrutinized by eye and manually rejected if they were erroneously detected “

Please explain.

Line 500

Were definitions of SW similar in vivo and in vitro? Were the conclusions from SW in vitro confirmed by SWs in vivo? The data seem mainly from slices.

Please explain deep learning in more detail. One has to read the results to infer how this was done and many other aspects of the methods. The figure legends are not very helpful in this regard, making it hard to read the paper.

Please explain in the methods what the authors mean by:

spatial entropy

RMSE

MDS space

binarized prediction

significantly predictive

SW identity number

chance level of spatial entropy

SW permeation by MC

Line 562

How was the subgranular zone defined? Consider a supplemental figure showing the method.

If slices were transverse, the DG is not a semicircle. If horizontal sections were made, it is not either. Therefore explain how the DG was simplified to a semicircle.

How was the edge of CA3 defined without a stain?

Statistics

Please add means and SEMs where n is the number of mice. This could be done in supplemental material.

Stats are not explained at all. This is a serious omission. For example, what were the parametric and non parametric tests, and what were the tests of normality to make these decisions? Or was it assumed all data were normal? Were ANOVA's two-way and if so were there interactions?

Figure 1

SW are not clearly SW. The traces are too compressed to tell. What are the criteria in vitro?

What are the criteria in vivo? If animals do not have immobility but are forced to be immobile, what relationship are the SWs of slices and anesthetized animals to SW in vivo in awake behaving animals?

For the expanded traces in Figure 1B what is the voltage calibration?

The traces need to be decompressed to tell when during the SW the MC activity starts. That is important so that one can tell if it was possibly monosynaptic or polysynaptic. However, it is recognized that with field potentials the onset of CA3 activity will be hard to know precisely. Therefore monosynaptic CA3-MC connections will be hard to confirm. If polysynaptic circuits are involved this is very important because it might be CA3 only activates MCs when secondary pathways become involved. Importantly, polysynaptic transmission is always variable compared to monosynaptic transmission. Together there are many reasons MC responses to SWs are variable as discussed above.

If MCs have different resting potentials in Figure 1B it would seem logical and not very informative to point out that their depolarizations in response to a SW are variable. An analysis of variability as it relates to resting potential could help. One reason is at depolarized potentials NMDA receptors will become important and broaden EPSPs of MCs.

If it is variable in the same MC at the same resting potential, that is nice but it is (1) not clear how much this has been observed (2) if that is surprising since SWs themselves are variable.

Figure 1 and elsewhere. Please add number of mice throughout.

I can't see traces in C. Here and elsewhere they are too small. Please explain MDS1 and MDS2. Furthermore, what are the traces from? What does the sphere of dots signify?

D. Based on the comments above, consider a plot of depolarizations that Is just for cells at a small range of membrane potentials to see if there is more consistency. Also consider other factors: latency from the onset of the SW, duration, area under the curve. Are these just as a variable or not? If in variable it would be insightful. Can variability be reduced by use of APV to block NMDA receptors, cutting away CA3a so only CA3b and c are present, or just c, etc? One could also block GC transmission with DCG-IV and GABAergic transmission to reduce polysynaptic influences.

In D, what is Vm# on the Y axis? Was this just done for the one slice with 5 MCs? What about other data? Was it reproduced? What was the finding here? Just that there is variability?

E. Why z standardize? What were the weak correlations (I just see one R value only) and were they statistically significant? what was the test?

Why are data from MCs pooled? In other words, why equate the 87 cells if they were from 23 slices and even fewer mice?

Here and elsewhere there are numerous impressive recordings from more than 1 MC. However, how are the relationships interpreted in MCs of the same preparation if sometimes there are 1, 2, and other times up to 5? One wonders because totals are often cited as if everything is pooled. Moreover, there is a correlation between the number of cells recorded in the same preparation and some outcomes. Because of that finding, I don't see that pooling is justified.

Figure 2. In B there is no GluR2/3 stain in the inner molecular layer where MC axons are located.

Why was 100-250 Hz used as a filter and what was the type of filter? Presumably this is to study ripples. But ripples are not typically considered over 200 Hz and below 100 Hz is often included. Also the figure shows ripples besides the two SW events- what were these- small SWs?

The inset needs a voltage calibration.

Figure 3. In A, the neural network is not explained thoroughly. What were the assumptions based on? What does a full connected link mean relative to one that is not connected? Why is there only unidirectional flow in light of the complex circuitry? What is the take home message in B, F? In C, what were the statistics? Please make symbols in D large enough to see. Explain the box and whisker plots. Were these data from one slice? Were they reproduced?

Please explain E.

Figure 4 Please explain the title. In A, what is the count of? In C, please explain the method of analysis of spatial entropy. The methods are not clear and the relationship of what is said in the methods about entropy to Figure 4C is not clear.

It seems here that it does not matter where the MC is located. Is that the message?

In D, E how was the single SW selected?

In Figure 5, What is "predicted deflection"? "dimensionally reduced"? What is the threshold for defining a SW event was predictable in A?

B. What is the spatial bias of a rate? Change distribution? Are "surrogates' the predicted events and non-surrogates are the actual SWs? What is the bottom line of this figure?

The very intriguing hypothesis in the abstract – i.e., a particular MC showed a more robust association with a particular SWR cluster, and the SWR cluster associated with one MC rarely overlapped with the SWR clusters associated with other MCs. – where is the evidence supporting this hypothesis? It seems only based on the complex analysis where there is a model driving the conclusions and the model may not be a good model.

Line 152. The authors find that the prediction error of real data was lower than shuffled data. Then they conclude from this that CA3 "information during SWs was at least partially preserved in the Vm responses of MCs" I see this as a major leap. All I see is that the deep learning had less of a prediction error for real data than shuffled data. Why is there an inference that this is meaningful in the way the authors state?

Line 160. The MCs were divided into subsets. Please explain what was done exactly. Why is it surprising that the more MCs are recorded simultaneously the better the prediction can be?

Line 169. Here the frequency range is 120-250 but in the figure it is 100-250.

Line 172. Please explain why the data suggest MCs "retain more information about SWRs"

Line 182. The SW waveform was predicted by the MCs but I am not sure that is interesting because the traces show that SWs are so similar from one example to the next. So it would be easy to predict.

Line 205. Only two intrinsic characteristics of MCs were examined so it seems hard to conclude that characteristics of MCs do not matter.

The fact that MCs in the area of the lower blade were more predictive could simply be due to greater connectivity with CA3 in that location. It would be good to investigate.

Line 211 What is meant by a dimensionality of SWs and reducing a SW to two dimensions?

The paragraph starting on page 224 is critical to the conclusion that is novel in the paper but it is not well explained. Therefore it is hard to be convinced. For example, is it justified to binarize prediction scores into 1 and 0? Is it reasonable to pool data from all MCs whether they were recorded with 1 other or 2 or more?

Reviewer #2 (Recommendations for the authors):

(1) Concerning more detailed model description

a – Details on model architecture: The manuscript briefly mentions the use of an encoder-decoder architecture with dense layers, but the rationale for choosing this architecture or the specific configuration of the layers used is not fully explained. The inclusion of such details, along with the rationale for the choice of activation functions (relu and sigmoid), would provide deeper insights into the model design.

b – Details on the training process: The paper would benefit from a more thorough explanation of the preprocessing steps applied to the data prior to training, as well as the rationale for the chosen loss function (root mean squared error, RMSE) and the detailed settings of the optimizer (e.g. learning rate, β values). This information is crucial for anyone attempting to replicate the study or apply the methodology to similar problems.

c – Details on data handling and evaluation metrics: Although cross-validation is mentioned, a clearer explanation of how the data sets were split and the criteria used for this split would be helpful.

d – Details on implementation and computational resources: Specifying the versions of TensorFlow, Keras and other dependencies used would help in replicating the computational environment. In addition, information about the required computational resources, such as GPU specifications (if applied), would provide practical insights into the feasibility of reproducing the study.

(2) Manuscript organization

The figures are effective in presenting the data, but the narrative in the text can be difficult to follow in places. Reorganizing the manuscript could facilitate better comprehension for readers. Specifically:

- Methodological descriptions should be confined to the Methods section.

- Theoretical and analytical concepts could benefit from succinct explanations where

they first appear.

- Transitions within the narrative should be smooth and well-motivated. For instance, the spatial analysis on page 7 requires a abrief introduction to provide context.

- A noteworthy result regarding the predictive value of MCs in relation to SWR information, currently discussed on page 11 (lines 300ff), could be more appropriately placed in the Results section.

(3) References

a – Hyde and Strowbridge (Nat Neurosci, 2012) have previously published research relevant to the topic; they used artificial stimuli to demonstrate encoding of temporal sequences into the MC network, suggesting mechanisms for short-term memory. The authors should acknowledge this study and discuss these earlier results in the context of their own findings.

b – Nitzan et al. (2020) undoubtedly serves as a valid reference for supporting the propagation of ripples from CA3/CA1 to cortical targets. However, since this phenomenon has previously been demonstrated and discussed, it would be preferable to cite earlier studies that originally identified or thoroughly investigated this propagation.

(4) Further comments

a – To maintain consistency in the literature, it is recommended that the authors align with established nomenclature. Specifically, 'SW' typically denotes slow waves, while 'SPW,' introduced by Buzsáki (1986) for sharp waves in the hippocampus, and SPW-R (or SWR), for sharp wave-ripple complexes, are the accepted terms. Using these conventions would enhance clarity and ensure alignment with the field's standard terminology.

b – "Input" versus "Response": The manuscript's language at times implies an active role of mossy cells. However, the analysis primarily concerns *synaptic inputs* from CA3 to MCs, indicative of upstream network dynamics, rather than direct responses (that is, spiking activity) of MCs. Since responses of MCs in the true sense were not the focus of this study, I recommend a thorough review and revision of the manuscript to accurately reflect this distinction.

c -Line 222f: "… a MC tended to predict a specific subset of SWs …" – A more appropriate (precise) formulation would imply that it is not MCs that predict a specific subset of SPWs, but the synaptic input that an MC receives from the upstream network.

d – Line 293: "Only a single MC was recorded in our in vivo study." – This sentence seems to be misleading: If I am not mistaken, the authors meant to write that their in vivo dataset consists of single MC recordings, as opposed to their in vitro dataset, which contains recordings of up to five MCs recorded simultaneously. Please rephrase this sentence.

e -Line 296: "…because the nerve fibers are preserved without sectioning in the in vivo preparations." – This statement, while not incorrect, is somewhat unspecific; the authors should perhaps specify that in vivo, CA3 projections targeting MCs are intact, resulting in a complete set of synaptic inputs related to CA3 network activity, as opposed to slices where connections are severed.

f -Line 313: "…the exponent α was 0.920 with a 99% confidence interval of [0.907,0.933]." – Please check the mathematical terminology used in the description of your equation. In the context of the given equation p=1−α^n, α serves as the base of the exponential term, and n is the exponent. Please correct.

g -Line 633: "… (in vivo) n = 273 SWs from 2 quintets." – Single MCs were recorded in vivo. Please correct.

h -Figure 2: The inset in panel B does not convincingly show the thorny excrescences. Can the authors add a microscopic image that shows this crucial feature of MCs more clearly?

i -Figure 3: Scale bars should be added to the traces displayed in panel B and F.

j -Figure S3: "Reproducibility of high frequency (120-250 Hz) increases…" – A more precise title would be "Reproducibility of 120-250 Hz coherence increases…"

k -Figure S4: The source of the predicted sharp wave/ripples (SWRs) is indicated as being from the CA3 region, yet the validation of prediction errors appears to be based on data from the CA1 region (main Figure 3). Please review and correct, if applicable.

Reviewer #3 (Recommendations for the authors):

1) Lines 69, 324: SWs do not propagate from CA3 to DG (other than volume conduction). Rather, the SW is a reflection in the LFP of local activity at the cellular level (spikes and synaptic inputs). It is the action potentials from CA3 cells that propagate the signal to drive mossy cells. I know what the authors mean, but it is important to be precise in one's language.

2) Line 72: SWs occur "primarily" during sleep and quiet wakefulness, but they also can occur during behavior, albeit much less frequently.

3) Line 73: "SWs represent a mechanism for reactivating or consolidating…." Although evidence in favor of this idea continues to accumulate, I don't think it is proven yet, and the words "are thought to" should appear before "represent".

4) Line 75: CA1 also outputs to the neocortex via direct projections back to deep layers of the EC

5) Line 80-81: The pioneering studies by Wilson & McNaughton (1994) and by Skaggs and McNaughton (1996) should be cited here.

6) Line 105: Do the authors mean "included" here? Why would you exclude cells with thorny excrescences on the dendrites?

7) Line 209: What does prediction "deflection" mean? This term is not defined.

8) Line 467: What was the purpose of exposing the mice to an enriched environment? I assume this was for a different study, but it should be clarified.

9) Figure S4 caption: The wording of this caption is confusing: "the SW of in vivo has a longer SW than that of in vitro"? Delete "that of"?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Distributed encoding of hippocampal information in mossy cells" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

The authors showed in their responses that they considered the concerns and took time to try to address the concerns. The efforts are appreciated. The manuscript is improved.

However, several of the concerns were not well addressed.

One issue that may not have been clear is that an explanation of the methods to construct a model of the network and the methods to use the model to develop the conclusions are not clear. This is critical so that the readers understand how the data were used to lead to the conclusions. In parts of the response some information is provided and this needs to be added to the manuscript. In addition, the additional methods need to be provided.

Some other fundamental concerns are raised by what the authors mention in their response:

If MCs were recorded for 55-367sec, how could the authors know (1) the cell was healthy, and (2) the cell was a MC? Regarding (1), how did the authors assess the health and stability of the recording? It would seem they could not so they simply assumed it was healthy, despite only keeping the recording for a short time which one would think implies the cell was not healthy. That should be stated in the methods, one would think. Regarding (2), it is stated that cells were filled with biocytin, and one is shown. If no time was available to determine if the cell was a MC by physiology, then the biocytin is critical to identify that the cell was a MC. Was it the case that all cells were identified as MCs by biocytin, or was it only a subset? If some cells were not stained or not stained well enough, why were they included? There are many large cells in the hilus that are not MCs so just the size of the soma is not a good way to tell if a hilar cell is a MC.

If MC depolarizations could not be analyzed by AUC or duration because there were barrages, this would be consistent with hilar cell physiology shown previously. The problem is that if barrages occur, one does not know if a SPWR caused a depolarization very well. This is because a SPWR has a duration that is 50-200 msec and barrages of EPSPs during that time will make it seem like MC depolarizations were caused by a SPWR but they actually occurred independently. A great way to make this easier is to use DCG-IV to stop the majority of MC spontaneous activity because it stops the GC input to MCs. If the authors do not choose to do this, then they need to make a better case that SPWRs induce MC depolarizations.

I apologize for not having read the Impact statement earlier. The current impact statement is quite complex, and the main message is not clear. Please revise.

There are several assumptions that are not clearly based on data in the literature

1. CA3 SPW-Rs are transmitted to the granule cells (GCs) via MCs. CA3 projects to both MCs and hilar GABAergic neurons. Together they innervate GCs, as well as each other. Therefore SPW-Rs in GCs are not necessarily a product of CA3 excitation of MCs alone. This was mentioned before and the authors added references that were suggested and content, which is good. But they added it in different locations. The Introduction still reads as if CA3 innervates MCs and MCs excite GCs, producing GC SPWRs. This is an oversimplification. Also, note that if the algorithm does not take into account the circuitry correctly it could make it seem like MCs are responsible for the events they call GC SPW-Rs and MCs are not solely responsible.

2. Please note it also is not clear to this reviewer that LFPs like SPWRs occur in the GC layer. What is it that the authors think are "SPWRs" in recordings of the GC layer? Depolarizations? Dentate spikes?

3. It is confusing if the term SWR is referring to the ripple or the SPW or both. This is because SWR is defined as a ripple 80-200 Hz in one location of the paper. Furthermore, if it is, how would MCs produce a ripple in GCs if GABAergic neurons are not invoked? This seems to be a major point of confusion.

4. What is the reason why "MC ensembles" are assumed? It seems there is no basis for this. MCs are not interconnected, or are not interconnected much. Perhaps the term "ensembles" is not what the authors mean?

On line 74-76, the references that are cited did not show that SPWRs travel from CA3 to the DG by MCs. Pentonnen et al. did not prove MCs were critical. It was merely suggested. Scharfman did not either.

Please explain the reasoning in the Introduction more clearly. For example, when are the authors discussing CA3 neurons and when are they discussion other neurons. When are they discussing the ripple and when are they discussing the sharp wave?

Please explain the meaning of overcapacity on line 424. Why do the authors state that MCs form a layer? They are heterogeneously distributed. Throughout the Discussion it seems that the authors are making statements of fact based on their network model and this is not appropriate. In the model, for example, if the make MCs a layer, that does not mean they are in vivo. Please specify in the Discussion that the results are what the neural network found, not the data (especially lines 418 and following)

Lines 434-437 are not clear. What the authors say they show is that CA3 has robust excitatory input to MCs, but this has been shown. Furthermore the authors seem to say they show MC activity occurs during SPWRs, but that has also been shown. On the other hand, one study did not find MC activity during SPWRs were not so consistent (Swaminathan et al.). The differences from the current study are not discussed.

Other points:

The response to the first comment is not very strong. The argument that the study proved connections between CA3 and MCs that have not been shown before is incorrect. Perhaps the authors are saying something else?

In response to the second point the authors say their study shows the extent to which SWRs are encoded in MCs. I do not see the authors showed this. That conclusion is based on a very simplified model and methods that they do not describe well.

Explanations in the response are not always added to the paper. Please do so.

Reviewer #3 (Recommendations for the authors):

The authors have addressed most of my points, but one of the major points is still unresolved.

Original comment 4: Although a mixed-effects model is preferable, the authors' new analyses are sufficient to show the same point, and this comment is considered resolved.

Original comment 5: The author's response is unsatisfactory. They acknowledge that the problem I raised was correct, but they continue to show the result of this flawed statistical analysis in Figure 3C. Instead, they add a new supplementary figure with a paired t test (the rebuttal letter and the main text (line 179) state that this is Figure 3-supp Figure 5, but I believe it is really Figure 3-supp Figure 1, as supp Figure 5 does not exist). They need to remove Figure 3C entirely from the paper, as it is an inappropriate test for the reasons described in the last review (and which the authors acknowledge). Instead, they should put Figure 3-supp Figure 1 in its place.

Original comment 6: The new discussion is a good addition. The authors should add Senzai and Buzsaki (2017) PMID: 28132824 and GoodSmith et al. (2017) PMID: 28132828 in the list of references with Bui et al. and Huang et al., as these papers were the first to show clearly that identified mossy cells had spatial tuning.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Distributed subthreshold representation of sharp wave-ripples by hilar mossy cells" for further consideration by eLife. Your revised article has been evaluated by Laura Colgin (Senior Editor) and a Reviewing Editor.

The manuscript has been substantially improved by your efforts but there are some remaining issues that need to be addressed, which can be summarized as follows:

1. Limitations about the identification of mossy cells should be noted. 2. Consider adding experiments with DCG-IV. 3. Revise the significance statement for clarity. Detailed recommendations are below.

Reviewer #1 (Recommendations for the authors):

Again, the authors have improved the paper with their revisions.

These residual concerns remain:

1. Identifying mossy cells electrophysiologically and morphologically.

The authors say that cells that "…had a membrane capacitance higher than 45 pF and spines and thorny excrescences on proximal dendrites …are electrophysiological and morphological markers of MCs."

A cell capacitance over 45 pF is insufficient to define MCs electrophysiologically because it is also a characteristic of other cells. Spines do not characterize MCs because they are present on other cell types. Thorny excrescences do but all cells were not filled by biocytin (and we don't know how many were out of all those included).

Therefore, please add a limitation to the text that the approach may have included other cell types, but the authors do not think this is a serious concern because the cells they filled showed thorny excrescences.

2. Regarding the evidence that CA3 SPWRs cause MC depolarizations

The authors say that they have shown that synaptic transmission to the MC via mossy fibers in not affected by SPWRs. However, that was not the point of the suggestion. The point was that blocking mossy fiber transmission is a useful tool to reduce the non-CA3 input. If experiments were done in this condition, it would be more convincing if a SPWR caused a depolarization in MCs because the input that is not from CA3, the majority, would be removed.

3. Regarding the Impact statement that was unclear

It is still unclear. Why is it important that 30% of SWR waveforms were reconstructed. How would a synaptic response of a MC reconstruct a SPR? How would 5 MCs do this?

Is this the meaning? Machine-learning algorithms combined with whole-cell patch-clamp of MCs and LFP recordings of SWRs showed MC EPSPs follow approximately 30% of SWRs?
