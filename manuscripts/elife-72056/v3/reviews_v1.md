# Peer review - Round 1

Editors:
- Virginie van Wassenhove, CEA, DRF/I2BM, NeuroSpin; INSERM, U992, Cognitive Neuroimaging Unit France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72056.sa0](https://doi.org/10.7554/eLife.72056.sa0)

To comprehend speech efficiently, the brain predicts what comes next as sentences unfold. In this study, Brodbeck and colleagues asked at which scale predictive processing helps the analysis of speech. The authors combined magnetoencephalography with state-of-the-art analyses (multivariate Temporal Response Functions) and information-theoretic measures (entropy, surprisal) to test distinct contextual speech models at three hierarchical processing levels. The authors report evidence for the coexistence of hierarchical and parallel speech processing supporting the independent contribution of local (e.g. sublexical) and global (e.g. sentences) contextual probabilities to the analysis of speech.


---

# Peer review - Round 1

Editors:
- Virginie van Wassenhove, CEA, DRF/I2BM, NeuroSpin; INSERM, U992, Cognitive Neuroimaging Unit France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72056.sa1](https://doi.org/10.7554/eLife.72056.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Parallel processing in speech perception: Local and global representations of linguistic context" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Barbara Shinn-Cunningham as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jonathan Brennan (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The sample size (N=12) appears like a low number, and authors should rationalize their sample choice with a power analysis, eventually illustrate with single-participant level data or explain why, in light of the paradigmatic strategy and analyses performed, this sample size is reasonable.

Reviewer 2 suggested that yuo contextualize a bit better how outcomes of Figure 7 fits other models (e.g. TRACE vs. RACE) and how the authors' novel observations update or modify existing architectures in the field.

Reviewer 3 questioned in his first main comment the choice of number of terms in the models being tested. The authors may wish to carefully address possible shortcomings of how more global models may leave room for local models to capture variance.

Reviewer 1 would like to see some justifications about why the analysis of phase-locked activity vs. induced responses is informative, and whether the latter could reveal additional insights if at all.

Additional suggestions made by all Reviewers should help clarify and streamline the manuscript further. Please keep in mind that the audience in eLife is diverse and readers may not necessarily be expert in (neuro)linguistics or technically versed with MEG. The overall flow of the manuscript can be streamlined a bit so as to clarify the complexity of some analyses that Reviewers 2 and 3 pointed out (some snippets are provided by Reviewer 1).

Reviewer #2 (Recommendations for the authors):

I had a few comments that I hope might help to make this paper even more impactful.

First, Figure 7 offers a boxology of the parallel processing architecture the authors believe is consistent with the data. Overall I'm pretty sympathetic to this view, but I would have liked to see the Discussion section better connect these conclusions with the existing literature. As presented, the reader might take the Figure 7 architecture to be a totally new model. I think it would be more appropriate to see how this updates or refines existing models. Specifically, I found myself reading the Discussion section through the lens of the late 90s debate on lexical access, specifically the TRACE model with fully interactive access, as compared to the RACE model of fully bottom-up access. I think the existing model can be recast as an extension of TRACE, but perhaps with the addition of "outputs" at each intermediate level (not just at the top?) I may not be exactly right here, but the upshot is I'd appreciate some extra handholding here for the reader to see how this architecture updates existing theories.

Second, the right lateralization of lower level effects seems to warrant further discussion. The interpretatin of these seems to emphasize the bilateral nature of speech perception – no arguments there – but the data actually favor a right-hemisphere bias which is unexpected to me (cf. the Giraud and Poeppel model for speech perception placed phoneme-level analysis predominantly in the left hemisphere).

Third, at N=12 the sample size is relatively low for 2021, and some key statistics are only reported as t_max. Together, I'm a little concerned that this may be a bit anti-conservative. At the least, I would like to see the statistics for reliable effects reproted as ranges (t_min – t_max). Increasing the N of the study would be great, but I understand if it is not feasible.

Figure 1: Where does meaning(j,i) come from? The red coloring seems to indicate it is the output of the sentence-level box, but that isn't clear to me from the sentence(i,j) notation.

ln. 255-256 – "While surprisal depends on the conditional probability of a discrete event and is agnostic to the underlying unit of representation". I don't understand this point. Both surprisal and entropy are calculated over distributions of some particular representation (P(phoneme_i|phoneme_i-1) ! = P(phoneme_i|word_j)… P(phoneme|…) ! = P(word|…)) I'm afraid I'm missing the intended point.

ln 702-704: I'm having trouble understanding the test for localization differences. I gather that the analysis takes source amplitude differences (180 or 176) per participant, and subjected these to a one-way anova, which was repeated for each pair of conditions. If so, shouldn't the DF for the F-test be (179, 11) or (175,11)? Instead, ln. 294-295 gives F(175,1925) and F(179 , 1969). I don't understand where that residual DF is coming from.
