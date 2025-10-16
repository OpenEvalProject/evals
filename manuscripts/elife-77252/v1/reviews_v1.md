# Peer review - Round 1

Editors:
- Manuel Zimmer, https://ror.org/03prydq77 University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77252.sa0](https://doi.org/10.7554/eLife.77252.sa0)

In this study, Bonnard and colleagues report a new method to assay feeding rates in C. elegans. Imaging fluorescence in the pharynx with subsequent image processing steps they make it possible to record pharyngeal pumping across freely behaving animal populations over periods up to 3 hs. They validate their method in different behavioural paradigms and with various feeding mutants.


---

# Peer review - Round 1

Editors:
- Manuel Zimmer, https://ror.org/03prydq77 University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.77252.sa1](https://doi.org/10.7554/eLife.77252.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Automatically tracking feeding behavior in populations of foraging worms" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Serena Ding (Reviewer #2).

Comments to the Authors:

We are sorry to say that, after consultation with the reviewers, we have decided that this work will not be considered further for publication by eLife. The reviewers found your work of high quality, and upon some revisions could represent a useful technique to study feeding behaviors in worms. However, the consensus of the reviewers was that your new method is useful only for this small circle of C. elegans researchers and therefore does not address the broader audience of eLife readers.

Please find their detailed comments and recommendations below.

Reviewer #1 (Recommendations for the authors):

(1) I think the authors did not fully exploit the great potential to perform long term observations in individual worms. I wonder whether they could perform experiments on single or few worms restricted to the imaging field of view so that they cannot collide and escape; thus, single worm identity is kept. How long is it possible to record without bleaching the pharyngeal marker? Is it possible to record over extended episodes, like feeding quiescence during lethargus or upon stress induction?

(2) Related to the above. Pumping rates in general show spread distributions, which I believe are not due to noise, please clarify. And under some conditions distributions show interesting bi-modality or skew e.g. Figure 4B (30min starvation) or unc-31 mutants (Figure 5F). Are inter-pump intervals autocorrelated and change smoothly in fed WT animals, and if yes on which timescales? Do 30min starved animals and unc-31 mutants switch between discrete states of high/low pumping rates and if yes, on which timescales. The authors report that they observed episodes of feeding quiescence, perhaps related to satiety quiescence. They could be more quantitative about this observation describing the time-scales and frequencies of these observations.

(3) The authors should be clearer about what n-numbers / sample sizes represent. Individual assays, worms used in assays (which would be less than data in the field of view), tracklets (which can be more than observed worms, see methods: 20-30s tracklets, meaning that many track interruptions could artificially blow-up the n-numbers) … ? E.g., in Figure 3 n numbers are in the hundreds; in Figure 3E two numbers are given in brackest. Please indicate these unambiguously in the Figure captions.

(3a) Depending on this, n numbers might be inaccurate in describing the real number of datapoints; or datapoints might not be independent of each other (e.g. many tracklets from the same worm). This affects the right choice of statistical testing procedures. Most figure panels that show comparisons lack any statistics.

(4) The authors state that a simple laptop/desktop would be sufficient but it seemed they used an HPC to generate the data in the manuscript. Please be clear about what the requirements really are and if the analyses are really feasible in a reasonable time using a standard computer. What were the CPU hours required to generate the data in this study?

(5) … "also find that similar to off-food reversals, which are constant throughout

larval development"… prior to this section the authors should explain better the general C. elegans behaviours known as some readers might not know what reversals are etc. For them, this comes out of nowhere.

(6) Figure 5D: the different contraction patterns should be qualitatively better described in the text so that readers get a better intuition of what causes the differences in the mean change images.

(7) The authors discuss a future outlook applying their method to 3D behaviour. For me, it is hard to imagine how this could ever work. Be precise, how this could be achieved realistically or remove this statement.

(8) …" using a rolling mean filter of 1 s and a smoothing filter of width =

66 ms (2 frames)": please be precise what the smoothing filter was, and why was this needed, since there is already a 1s rolling mean applied.?

Reviewer #2 (Recommendations for the authors):

– This new method directly measures the pumping of the pharyngeal muscles as a proxy for feeding. However, worms are also known to pump their pharynx without actual food intake, such as when off-food. The authors should be more explicit about this limitation to their method and take care when using "pumping" and "feeding" interchangeably.

– One key advantage of this new method is that pumping and locomotion behaviour can be simultaneously detected to generate new insights e.g. regarding behavioural modularity and coordination. However, the authors report that while the pumping rates remain the same whether imaging with YFP or mCherry, other locomotion metrics such as velocity are different. This result thus calls for careful interpretation in future studies that link both types of behaviours using this method.

– The first sentence of the introduction (p.1) "Animals must forage… and provide for their young" is perhaps too generalised. There are animals that do not provide for their young, so I suggest removing this part of the sentence.

– Page 8, middle paragraph: multiple exposure vs. single exposure experimental differences "could be due to … different remaining food levels". Why would this be, if the experiments and feeding rates are reported to be the same in both cases?

– "Pharaglow" is capitalised in some cases and not others.

– Perhaps the authors could also comment on what happens when animals overlap during the experiment, especially in the context of large scale foraging experiments.

Reviewer #3 (Recommendations for the authors):

Detailed comments:

The term "worm" is highly nonspecific, encompassing 3 phyla.

"C. elegans" or better yet "Caenorhabditis elegans" should be in the title.

The Introduction focuses somewhat narrowly on studies of foraging strategies and food intake. In addition to these interesting topics, the authors could discuss how assessment of feeding is used in studies of behavioral genetics, quiescence, and aging.

I found the description of pharyngeal pumping in the introduction to be quite confusing. The authors should strive to use standard anatomical and behavioral terms and explain them for the naive reader. For example, the sentence "Transport proceeds with occasional peristaltic contractions that move food further toward the intestine where a hard cuticular structure, the grinder, crushes the bacteria before they are pushed into the intestine" needs to be rephrased. The peristaltic motion is called isthmus peristalsis. It moves food particles to the terminal bulb which contains the grinder.

"Of these motions, pumping is the most frequent contraction that is also the limiting step for food intake". I am lost as to what was intended here.

Figure 1F: Why is the y axis given as arbitrary units? I would like to see how large the variation in standard deviation is during pharyngeal pumping.

The comparison between automated assessment and expert manual assessment is weak because both were done with low-resolution fluorescence data. If the goal is to compare with how pharyngeal pumping is normally assessed, the authors should use high-resolution bright field or DIC images, as

Another problem with the automated/manual comparison is that the pumping rate varied over a fairly narrow range. As the authors acknowledge, pumping is modulated by many different factors, so it is not difficult to prepare worms with a wide range of pumping rates. Doing this would help assess linearity of the method, especially at low pump rates.

The sections describing various applications of the method (development, starvation, and mutants) are poorly motivated and written in a confusing manner. For each section the authors need to briefly introduce the questions being addressed and why they are important. Similarly, the results should be briefly discussed in light of the questions being asked.

Page 7: "We find that on-food pumping rates increase slightly over the course of the larval stages, but much less dramatically than the velocity." Why are the authors comparing the increase in pumping rate with velocity? These are like apples and oranges.

The authors cite results showing that long-term exposure to light reduces lifespan. But to test for phototoxicity, the authors measure not lifespan but feeding rate! This seems odd. A simple experiment would be to keep the illumination on until all the animals have died. This would give some indication of how close to a lethal dose is being delivered to the worms.

Figure 3: The ordering of the panels here is confusing.

3C,3D: Specific Y axis labels would be better here. Why not measure area in µm^2? Why not have axes for pumping rate in Hz and velocity in mm/s?

Page 10: "…the distributions of both pumping rates and velocities show distinct sub-populations". I see no evidence of subpopulations in velocity. There are some local maxima and minima in the pumping rate, but without further analyses these effects seem quite preliminary.

Page 12. "It is possible that some of the detected pumps in our measurements are either peristaltic movements or other non-productive muscular motion". The authors imply that isthmus peristalsis is "non-productive", which does not make sense to me. Have the authors observed isthmus peristalsis in their images? It should be straightforward to see if isthmus peristalsis is reflected in the traces shown in Figure 1F.

Page 16: "labeling parts of the pharynx with lipophilic dyes would be a possibility to extend the usage of this tool beyond species that are genetically tractable". I do not understand how lipophilic dyes, which label certain structures but not the pharynx, would be useful here.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Automatically tracking feeding behavior in populations of foraging worms" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior Editor) and a Reviewing Editor. I am happy to tell you that all reviewers are now very enthusiastic about your manuscript, which has been significantly improved. However, there are some remaining issues raised by reviewer #1 that need to be addressed, as outlined below.

Reviewer #1 (Recommendations for the authors):

In this revision, the authors have made some efforts to address my review points. My main point, however, which was to prove the suitability of their approach for long term observations with subsequent analyses is only partially addressed.

(1) It is very promising to see that there is almost no bleaching of the pharyngeal signal; this does not mean however that these experiments work practically for extended recording times of more than one hour (see #2 below). I suggest being more careful with the conclusions.

(2) The authors show an impressive example of male-hermaphrodite interactions recording behaviors over a period of 1h. This is great, but unfortunately just one example. Is this the best outcome the authors could have ever achieved or is it representative for many experiments? With the male-hermaphrodite paradigm, the authors go beyond what I was requesting. If their approach works as they claim, it should be feasible to perform a sufficient amount of single animal recordings.

(3) The authors attempted to address one of my points showing pumping rate distributions of individual animals (2H, 3G). I disagree with the authors statement that PharaGlow can "produce large animal statistics while preserving single worm behavioral information". This ability is hampered by the short tracklet durations. One cannot conclude from e.g. 3G left panel whether individuals differ in an idiosyncratic way versus transient changes that are randomly captured in the short tracklet episodes. Hence, my previous request to perform statistics on longer recordings. Figure 5D indicates that the animals exhibit minutes lasting episodes of high and low pumping rates. More 1h recordings on individuals like in Figure 5 (perhaps no need to do male plus hermaphrodite) will enable the authors to perform the requested analyses. As mentioned above, if PharaGlow performs as the authors claim, these revisions should be doable with reasonable effort.

Reviewer #2 (Recommendations for the authors):

The authors have thoroughly and effectively responded to previous reviews, resulting in a significantly improved manuscript. It is now clear that the method is broadly applicable using common imaging microscopes and computing resources, and that it is suitable for studying pumping behaviour in populations of unrestrained animals across various time- and space- scales. The method affords novel observations not directly feasible with previous methods, for instance, exemplified by the authors' recent addition of pumping dynamics during mating events.

Reviewer #3 (Recommendations for the authors):

The statistical tests added to the paper were not reported correctly. There are multiple instances of "p<0.000" and ""p=0.000" in the figures and captions. In fact every single p value given in Figure 4 and its caption is either zero or negative! Similarly in Figure S2.2A , S2.5A.

But in general the revised manuscript is much improved compared to the original.
