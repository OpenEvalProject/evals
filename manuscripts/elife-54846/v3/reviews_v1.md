# Peer review - Round 1

Editors:
- Chris I Baker, National Institute of Mental Health, National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54846.sa1](https://doi.org/10.7554/eLife.54846.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript presents a detailed and in-depth study of word processing, providing evidence that a compositional letter code potentially makes a major contribution to word reading and can account for reading of jumbled words. One of the major strengths of this work is the combination of careful behavioral experiments, a simple neural model based on properties of neurons in monkey IT cortex, and fMRI data in human participants.

Decision letter after peer review:

Thank you for submitting your article "A compositional letter code in high-level visual cortex explains how we read jumbled words" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Chris I Baker as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Floris de Lange as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The reviewers find the manuscript describes a very interesting and detailed study of the potential contribution of a compositional letter code to word reading using novel approaches across behavioral and neuroimaging data. A simple model of responses to individual letter shapes can explain performance in visual search tasks and capture some aspects of word and non-word processing. Further, neuroimaging data suggests that the compositional letter code corresponds to processing in a region in lateral occipital cortex, with the visual word form area (VWFA) corresponding to processing of properties related to word knowledge. One of the major strengths of this work is the combination of careful behavioral experiments, a simple neural model based on properties of neurons in monkey inferotemporal cortex, and fMRI data in human participants.

While the manuscript is well-written and comprehensive, the reviewers felt there are a number of revisions that would strengthen the work. These revisions would require significant reframing of the manuscript to more accurately reflect the data and the existing literature.

Essential revisions:

1) The conclusions tend to be overstated. The manuscript provides an interesting demonstration of what a visually based model can accomplish, but the authors go too far in their interpretation. The compositional letter code explains aspects of word and non-word processing, but not everything related to word reading. For example, in the lexical decision task, response times for words are explained by word frequency and there will be contributions from semantics, especially when reading strings of words/sentences. The authors should be clearer in describing what the data show and not over-reach into an account of word reading that discounts other factors without justification. This will also require a change in the title of the paper since most of the tasks the authors employ are not about word reading.

2) Related to point (1), the authors make a series of assertions that are not supported by their data and also present an oversimplified and somewhat biased review of the literature. The authors should clarify and justify these assertions. In particular:

a) "we hypothesized that word reading is enabled by a purely visual representation". There is a large and robust literature demonstrating how various linguistic properties have substantial effects on word recognition and the authors should acknowledge and cite this literature.

b) Visual search is very different than reading. It should be made clear that this task is not a test of the more general computations involved in reading.

c) "This difference in visual similarity explains why transposing the middle letters renders a word easier to read than transposing its edge letters". The authors should more clearly explain or qualify this assertion.

d) The two sentences in the Introduction seem to contradict each other. It is first suggested that word reading could be explained by a purely visual code, but then it is stated that reading could be a confound. It seems that what the authors want to say is that many different tasks involving words can (but are not necessarily always) be achieved by visual computations. This is a different claim than what is written throughout the paper.

e) The work as presented is not a test of the hypothesis that cortical regions involved in word recognition have tuning for letter combinations. Evidence for this hypothesis is based on a very different paradigm and the effect has been replicated by at least 3 different labs. The authors should clearly explain how the phenomenon they report aligns with those data.

f) Conceptually it is unclear how the bigram model lines up with the main assertion of the manuscript that performance can be understood in terms of the summation of performance for single letters. As soon as additional weights are added for bigrams isn't this akin to saying that there is a different representation of bigrams than of individual letters?

g) "According to an influential account of word reading…. ". This influential account of word reading is about the word recognition process not the detection of bigrams in a search array. It makes no comment or prediction about how the proposed neurons would be involved in the tasks developed by the authors. This is not to say that the model of bigram detectors in word-selective cortex is correct, just that the present work can be seen as orthogonal to this model and the authors need to clarify and justify how their data relates.

h) Subsection “Experiment 5: Lexical decision task” – why is the model retrained? If the model based on letters in general is used in this task shouldn't the same weights be used?

i) The summary sentence "In sum, we conclude that word response times are explained by word frequency and nonword response times are explained by the distance between the nonword and the nearest word calculated using the compositional neural code." accurately captures what the data show. It highlights how the authors' model makes interesting predictions in a variety of contexts. But it also contradicts the main assertions laid out in the Introduction as they note that many factors that are not purely visual explain a major portion of the variance.

j) Some of the findings on the fMRI task have been reported a number of times in the literature (e.g. the difference in VWFA response to words and pseudowords). The manuscript would be strengthened by relating it to these previous studies.

3) The authors find that LO is the region that is most sensitive to their visual similarity metric.

a) Given prior work showing the critical role of VWFA in reading, this result would seem to suggest that visual similarity is not at the core of reading per se and this issue should be discussed.

b) The paragraph beginning with "To further investigate the link between the compositional…" needs clarifying. Further, prior work has focused on the VWFA for the claim of bigram detectors and the authors needs to explain how the finding of a compositional code in LO relates to that work.

c) The authors also show that LO has a representation of semantic space. This suggests a contribution beyond visual properties. What does this mean for the role of these neurons? What are the implications of this overlap for theories of orthographic and semantic processing? This needs to be discussed.

4) Some results do not seem to support the ideas of the paper, but are framed as doing so. Specifically:

a) "To quantify this observation, we asked whether the model error for each bigram pair, calculated as the absolute difference between observed and predicted dissimilarity, covaried with the average bigram frequency of the two bigrams (for both frequent bigrams and words). […] We conclude that bigram search can be explained entirely using single neurons tuned to single letters."

The significant negative correlation does not seem to fit with the later statement that "model errors are not systematically different for frequent compared to infrequent bigram pairs". The authors should clarify this point in this paragraph, but also explain how this result fits with main message of the paper. There are a number of effects that are against the idea the main hypothesis "that word reading is enabled by a purely visual representation" and that the model "explained human performance in both visual search as well as word reading tasks." (Abstract). For instance, the effect of familiarity on asymmetric spatial summation (subsection “Experiment 3: Upright versus inverted bigrams”), and the frequency effect (Experiment 5).

b) If the claim is "there are no specialized detectors for letter combinations", it's not clear how Experiment 5 (where the same letters in different orders give different RTs) fits with this. This seems to strongly support a role for particular letter combinations.

5) In the analysis of mean VWFA activity, response times do not seem to be controlled. This is important because RTs might influence the magnitude of the β coefficients in a systematic way that does not directly correspond to the relevant processing. These should be included in the model.

6) In a number of places in the manuscript, the authors draw conclusions about how neurons are tuned, but without directly recording from neurons, it is not possible to draw this conclusion. For example, "Our main finding is that viewing a string activates a compositional letter code, consisting of neurons tuned to single letters whose response to longer strings is a linear sum of single letter responses".

7) It was mentioned that outliers in dissimilarity values across subjects were removed using built-in routines in MATLAB (isoutlier function, MATLAB R2018a). This is unusual and not typically seen in dissimilarity analyses. Are the findings the same without this procedure? How many outliers are removed? How is this threshold calculated/selected?

8) The manuscript mentions that cross-validation was performed but details on this are absent. In any case, pairwise dissimilarity calculations should be performed across runs (i.e., not correlating between items in the same run). This is particularly true because the trials are close together and influenced by the adjacent BOLD response.

9) It would be worth discussing how these findings relate to results (and associated theories) regarding whether individuals and specifically the VWFA process orthographic stimuli in a holistic versus part-based fashion (e.g., Carlos et al., 2019). More generally, behavioral responses to inverted words are relevant to this work, and worthy of more discussion (for how such findings are, or are not, consistent with this manuscript).

10) The authors report an exhaustive series of experiments and there is extensive supplementary material – while the authors should be commended for providing so much material, it does make the manuscript challenging to read at times, requiring the reader to jump around different parts of the text to fully understand the methods and results. The authors should include information such as the number of subjects in each experiment and key aspects of the stimuli (total number, how selected etc.), and protocol (e.g. timing of stimulus presentation, stimulus size etc.) in the main text. Further, there appears to be some inconsistency between the naming of sections. In the main text the authors refer the reader to, for example, "Section S7", but the supplementary material itself is labelled as "Section A7", and the tables and figures are numbered sequentially throughout the supplementary material such that the relevant figure in "Section A7" might be "Figure S16" – all very confusing. The authors should reconsider how they are structuring the supplementary material to make it more intuitively organized.
