# Peer review - Round 1

Editors:
- Miriam Spering, The University of British Columbia Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91243.3.sa0](https://doi.org/10.7554/eLife.91243.3.sa0)

This fundamental study has the potential to substantially advance our understanding of human locomotion in complex real-world settings and opens up new approaches to studying (visually guided) behavior in natural settings outside the lab. The evidence supporting the conclusions is overall compelling. Whereas detailed analyses represent multiple ways to visualize and quantify the rich and complex natural behavior, some of the specific conclusions remain more suggestive at this point. The work will be of interest to neuroscientists, kinesiologists, computer scientists, and engineers working on human locomotion.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91243.3.sa1](https://doi.org/10.7554/eLife.91243.3.sa1)

Summary:

The work of Muller and colleagues concerns the question where we place our feet when passing uneven terrain, in particular how we trade-off path length against the steepness of each single step. The authors find that paths are chosen that are consistently less steep and deviate from the straight line more than an average random path, suggesting that participants indeed trade off steepness for path length. They show that this might be related to biomechanical properties, specifically the leg length of the walkers. In addition, they show using a neural network model that participants could choose the footholds based on their sensory (visual) information about depth.

Strengths:

The work is a natural continuation of some of the researchers' earlier work that related the immediately following steps to gaze. Methodologically, the work is very impressive and presents a further step forward towards understanding real-world locomotion and its interaction with sampling visual information. While some of the results may seem somewhat trivial in hindsight (as always in this kind of studies), I still think this is a very important approach to understand locomotion in the wild better.

Weaknesses:

The concerns I had regarding the initial version of the manuscript have all been fixed in the current one.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91243.3.sa2](https://doi.org/10.7554/eLife.91243.3.sa2)

This manuscript examines how humans walk over uneven terrain and use vision to decide where to step. There is a huge lack of evidence about this because the vast majority of locomotion studies have focused on steady, well-controlled conditions, and not on decisions made in the real world. The author team has already made great advances in this topic by pioneering gaze recordings during locomotion, but there has been no practical way to map the gaze targets, specifically the 3D terrain features in naturalistic environments. The team has now developed a way to integrate such measurements along with gaze and step tracking. This allows quantitative evaluation of the proposed trade-offs between stepping vertically onto vs. stepping around obstacles, along with how far people look to decide where to step. The team also introduces several new analysis techniques to accompany these measurements. They use machine learning techniques to examine whether retinocentric depth helps predict footholds and develop simulations to assess possible alternative footholds and walking paths. The technical achievement is impressive.

This study addresses several real-world questions not normally examined in the laboratory. First, do humans elect to walk around steeper footholds rather than over them? Second, is there a quantifiable benefit to walking around, such as allowing for a flatter path? Third, does visual depth of terrain contribute to selection of footholds? Fourth, are there scale effects, where for example a tall adult can easily walk over an obstacle that a toddler must walk around. One might superficially answer yes to all of these questions, but it is highly nontrival to answer them quantitatively. As for the conclusions, my feelings are mixed. I find strengths in answers to two of the questions, and weaknesses in the other two.

Strengths:

I consider the evidence strongest for the first of the main questions. The results show subjects walking with more laterally deviating paths, measured by a quantity called "tortuosity," when the direct straight-ahead paths appear to have steeper ups and downs (Fig. 9). The measure of straight-ahead steepness is fairly complicated (discussed below), but is shown to be well correlated with tortuosity, effectively predicting when subjects will not walk straight ahead.

There is also good evidence for the third question, showing that retinocentric depth is predictive of chosen footholds. Retinocentric depth was computed by a series of steps, starting with scene capture to determine a 3D terrain mesh, projecting that mesh into the eye's perspective, and then discarding all but the depth information. This highly involved process is only the beginning, because the depth was then used to train a neural network classifier with chosen footholds. That network was found to predict footholds better than chance, using a test set independent from the training set, each using half the recorded data. The results are strong and are best interpreted along with a previous study (Bonnen et al. 2021) showing that subjects gaze nearer ahead on rougher terrain, and slightly more so when binocular vision was disrupted. Depth information seems important for foothold selection.

As an aside, humans presumably also select footholds and estimate depth from a number of monocular visual cues, such as shading, shadows, color, and self-motion information. Interestingly, the terrain mesh and depth data here were computed from monocular images, suggesting that monocular vision can in principle be predictive of both depth and footholds. Binocular human vision presumably improves on monocular depth estimation, and so it would be interesting to see whether binocular scene cameras would predict footholds better. In an earlier review, I had suggested other avenues for exploration, but these are not weaknesses so much as opportunities not yet taken. I believe much could be learned from deeper analysis of the neural network, and future experiments using variations of this technique.

There is much to be appreciated about this study. I was impressed by the overarching outlook and ambitiousness of the team. They seek to understand human decision-making in real-world locomotion tasks, a topic of obvious relevance to the human condition but not often examined in research. The field has been biased toward well-controlled, laboratory studies, which have undeniable scientific advantages but are also quite different from the real world. The present study discards all of the usual advantages of the laboratory, yet still finds a way to explore real-world behaviors in a quantitative manner. It is an exciting and forward-thinking approach, used to tackle an ecologically relevant question.

I also appreciate the numerous technical challenges of this study. The state of the art in real-world locomotion studies has largely been limited to kinematic motion capture. This team managed to collect and analyze an unprecedented, one-of-a-kind dataset. They applied a number of non-trivial methods to assess retinocentric depth, simulate would-be walking paths and steepness, and predict footholds from neural network. Any of these could and probably will merit individual papers, and to assemble them all at once is quite beyond other studies I am aware of. I hope this study will spur more inquiries of this type, leveraging mobile electronics and modern machine learning techniques to answer questions that were previously only addressable qualitatively.

Weaknesses:

Although I am highly enthusiastic about this study, I was not entirely convinced by the evidence for the second and fourth questions. Some of this is because I was confused by aspects of the analysis, limiting my understanding of the evidence. But I also question some of the basic conclusions, whether the authors indeed proved that (from Abstract, emphasis mine) "[walkers] change direction TO AVOID taking steeper steps that involve large height changes, instead of [sic] choosing more circuitous, RELATIVELY FLAT paths." (I interpret the "of" as a typo that should have been omitted). I think it is more objective to say, "walkers changed direction more when straight-ahead paths seemed to have steeper height changes."

I say "seemed" because it is unknown whether humans would have experienced greater height changes if they walked straight ahead (the second main question). The comparison shown is between human tortuous paths taken and simulated straight-ahead paths never experienced by human. Ignoring questions about the simulations for now (discussed below), it is not an apples-to-apples comparison, say between the tortuous paths humans preferred and straight-ahead paths they didn't. The authors determined a measure of steepness, "straight path slope" (Fig. 9), that predicts when humans circuitously, but that is the same as the steepness that humans would actually experience if they had walked straight ahead. That could have been measured with an appropriate control condition, for example asking subjects to walk as straight ahead as they can manage. That also would have eliminated the need for simulations, because the slope of each step actually taken could simply have been measured and compared between conditions. Instead, two different kinds of simulations are compared, where steeper paths are fully simulated, and the circuitous paths are partially simulated but partially based on data. It seems that every fifth circuitous step coincides with a human foothold, but the intervening ones are somewhat random. I don't find this especially strong evidence that the chosen paths were indeed relatively flatter. I would prefer to be convinced by hard data than by unequal simulations.

I also have trouble accepting "TO AVOID" because it implies a degree of intent not evident in the data. I suppose conscious intent could be assessed subjectively by questionnaire, but I don't know how unconscious intent could be tested objectively. I believe my suggested interpretation above is better supported by evidence.

My limited acceptance is due in part to confusion about the simulations. I was especially confused about the connection between feasible steps drawn from the distribution in Figure 7, and the histograms of Figure 8. The feasible steps have clear peaks near zero slope, unity step length, and zero step direction (let's call them Flat). If 5-step simulations of Figure 8 draw from that distribution, why is there zero probability for the 0-3 deg bin (which is within {plus minus}3 deg due to absolute values)? It seems to me that Flat steps were eminently available, so why were they completely avoided? It seems that the simulations were probabilistic (and not just figurative) random walks, which implies they should have had about the same mean as Figure 7 but a wider variance, and then passed through absolute value. They look like something else that I cannot understand. This is important because the RELATIVELY FLAT conclusion is based on the chosen walks apparently being skewed flatter than random simulated walks. I have trouble accepting those distributions because Flat steps were unaccountably never taken by either simulation or human. (This issue is less concerning for Figure 9, because one can accept that some simulation measure is predictive of tortuosity even if the measure is hard to understand).

I was also confused why Figure 7 distances and directions are nearly normally distributed and not more uniform. The methods only mention constraints to eliminate steps, which to me suggests a truncated uniform distribution. It is not clear to me why the terrain should have a high peak at unity step length, which implies that the only feasible footholds were almost exclusively straight ahead and one step length away. It is possible that the "feasible" footholds are themselves drawn from a "likely" normal distribution, perhaps based on level walking data. It could be argued that simulated steps should be performed by drawing from typical step distributions for level ground, eliminating non-viable footholds, and then repeating that across multiple steps. That would explain the normality, but it is not stated in the Methods, and even if they were "feasible and likely" it would not explain the distributions of Figure 8.

I had some misgivings about the fourth question, where Figure 10 suggests that shorter subjects had greater correlation between straight-path slope and tortuosity than taller ones, who tended to walk straighter ahead. I agree with the authors' rebuttal to my previous review that "the data are the data" but I still have doubts. Now supplied as suggested by another reviewer, Figure 18 provides more detail of the underlying data, with considerably lower correlations. I now suspect that Figure 10 benefits from some statistical artifacts due to binning and other operations, and the weaker correlations of Fig. 18A are closer to reality. I am rather suspicious of correlations of correlations (Figure 18B), which lose some statistical grounding because the second correlation treats all data on equal footing, effectively whitewashing the first correlations of their varying significance (p-values 0.008 to 1e-9).

Furthermore, I am also unsure about Figure 10's comparison of tortuosity vs. straight path slope against leg length. Both tortuosity and straight path slope are already effectively dimensionless and therefore already seem to eliminate scale. It is my understanding that the simulated paths were recomputed for each subject's parameters, and the horizontal axis, slope, is already an angular measure that should affect short and tall people similarly. Shouldn't all subjects equally avoid steep angles, regardless of their dimensional height? If there is indeed a scale effect, then I would expect it to be demonstrated with a dimensional measure (vertical axis) that depends on leg length.

I certainly agree with the hypothetical prior that tall adults walk straight over obstacles that shorter adults (or children) walk around. But I feel that simpler tests would better evidence, perhaps in future work. Did shorter subjects walk with greater tortuosity than taller ones on the same terrain? Did shorter subjects take relatively more steps even after normalizing for leg length? A possible comparison would be (number of steps)*(leg length)/(start to end distance). I feel that the evidence from this study is not that strong.

Although it is a strength of this study that so much can be learned from pure observation, that does not mean controlled conditions are not scientifically helpful. As mentioned earlier, a helpful control could have been to ask subjects to walk straighter but less preferred paths on the same terrain, treating human paths as an independent variable. Another would be to treat terrain as an independent variable, by using level ground and intermediate terrain conditions. This would make it easier to test whether taller subjects walk straighter ahead on more uneven terrain than shorter subjects. Indeed, the data set already includes some patches of flatter terrain, not included here. Additional and simpler tests might be possible based on existing data.

Conclusion

This is an ambitious undertaking, presenting a wealth of unprecedented data to quantitatively test basic ecological questions that have long been unanswered. There are a number of considerable strengths that merit appreciation, especially the ability to quantitatively predict when humans will walk more circuitously. The weaknesses are about limitations in the conclusions that can be drawn thus far rather than the correctness of the study. I consider this to be a first step that will hopefully enable and inspire a long line of future work that will address these questions more in depth.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91243.3.sa3](https://doi.org/10.7554/eLife.91243.3.sa3)

Summary:

The systematic way in which path selection is parametrically investigated is the main contribution.

Strengths:

The authors have developed an impressive workflow to study gait and gaze in natural terrain. They are able to determine footholds and gaze points in the 3D world, and explore different path selections in the terrain.

Weaknesses:

The finding that walkers prefer less tortuous, demanding paths is hardly surprising, and from the data it is still not clear what actual visual features are used to choose among alternative routes or what the nature of the decision process is. The authors discuss energetic cost and other "factors" that might influence path selection, but as yet there is no way to express these ideas rigorously in such complex natural settings.
