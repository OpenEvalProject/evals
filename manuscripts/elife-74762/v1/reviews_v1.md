# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74762.sa0](https://doi.org/10.7554/eLife.74762.sa0)

This paper tests hypotheses for the role of INaP and ICAN in the preBötC, the region of the brainstem that generates inspiratory breathing rhythm, using optogenetic manipulation of local preBötC excitability and pharmacologic blockade of INaP and ICAN and tests resulting predictions about these currents using computational simulation. The paper will be of interest to respiratory researchers and all those interested in neuronal rhythm generation.


---

# Peer review - Round 1

Editors:
- Ronald L Calabrese, https://ror.org/03czfpz43 Emory University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74762.sa1](https://doi.org/10.7554/eLife.74762.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Predictions and experimental tests of a new biophysical model of the mammalian respiratory oscillator" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by Ronald Calabrese as the Senior and Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Luis Rodrigo Hernandez-Miranda (Reviewer #1); Christopher Wilson (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. The experimental data rest in large part on ChR2 providing essentially a step depolarization specifically and uniformly to preBotC glutamatergic neurons. However, ChR2 stimulation appears to produce some unexpected and unexplained effects of ChR2 stimulation that are not reproduced in the model and that may result from ChR2 expression in glutamatergic terminals from non-preBotC neurons and perhaps incomplete light activation of deeper neurons (off target effects). In particular there is concern that the post-stimulus inhibition appears to be a significant effect that is not replicated by the model and suggests that assumptions about ChR2 in the model require greater scrutiny. Absent further development of the model to encompass this phenomenon the claim that the experiments fully confirm model predictions should be scaled back.

2. The authors' attempts to resolve the conflicting data for the INaP necessity hypothesis in the Discussion overlooked experimental details in papers that counter the authors arguments. For example, Pace et al., (2007) showed that bilateral microinjection of riluzole or low concentrations of TTX into preBötC failed to stop the rhythm and that the pharmacological effects of these blockers could be explained by their effects on raphe excitability, which provides tonic excitatory drive to the preBötC. The authors propose that these conflicting results can be explained by differences in slice thickness and incomplete pharmacological penetration; however, the Pace paper specifically addressed this issue by microinjecting the drugs 100 μm below the surface. This could, of course, still lead to differences in penetration and there are still differences in the amount of network in the slice, but the discussion of thick vs. thin omits needed details here, and these effects can be addressed experimentally, in future. Absent such future experiments the conclusion that INaP is essential for must be removed and replaced by a more balanced conclusion.

3. Reviewer #3 asked for more detail about individual bursting neurons and their firing profiles because the relative expression of gNaP is important for endogenous bursting neurons. So, the authors would have a stronger argument if they included gNaP/Cm (as was done in the Koizumi et al., (2008)) and then showed what happens to those individual neurons when INaP and I_CAN are blocked. That would speak to questions re: variability in rhythm and give an idea of just how much INaP is present in the neurons recorded.

4. Please address the statistical issues brought up by the reviewers.

5. Please provide the missing details of the model requested by the reviewers.

6. Each reviewer provides detailed comments that will supplement and expand this summary.

Reviewer #1 (Recommendations for the authors):

In the current study, Phillips at al., experimentally tested three prediction that emerged from a previously published computational model (eLife 2019, 8:e41555): (1) the blockade of ICAN and INaP produces opposite effects on preBötC rhythmic activity; (2) ICAN is essential for preBötC rhythmogenesis; and (3) ICAN is key for generating the amplitude of respiratory rhythmic output. To do so, the authors used optogenetic/pharmacologic stimulation of the preBötC on mouse brainstem slices. These three predictions are, to a large extend, demonstrated with the new provided experimental data. Globally, the new findings reported by Phillips and colleagues foster our understanding on the elusive mechanisms that underline the generation of the respiratory (more precisely inspiratory) rhythm in mammals, which are of great interest for researchers working in respiratory physiology.

Comments

1. I have no problems with the model simulations/predictions nor with the findings of this carefully done work. Nevertheless, in my view, it is written in a highly technical manner that is not accessible to neuroscientists working on areas distinct to electrophysiology/computational modeling, which might preclude the full understanding of this very interesting study. Therefore, I would suggest to the authors to work a little bit on making this study more accessible to the large readership of eLife.

2. One aspect that could perhaps be discussed in this work is if Phillips's model could also consider the interconnections existing between left/right preBötC in rhythmogenesis and population activity amplitude. In other words, can the current computational model predict how ipsilateral changes in ICAN and INaP might alter population activity amplitude and rhythmogenesis on the contralateral preBötC?

Reviewer #2 (Recommendations for the authors):

Connectivity has been shown to be an important parameter in preBötC dynamics and was explored in the previous publication of this model, but the connectivity matrix/synaptic parameters are not described in this text and should be included.

Data from the model showing how optogenetic stimulation in the model compares to experimental results, particularly with respect to poststimulation membrane polarization and network effects, e.g., inhibition of rhythmicity following stimulation, should be presented.

In "Model Tuning", changed parameters are stated to be marked in red, but there is no red text; although, some values/terms do appear to be slightly bolded. Please use a clearer mark that is color-blind friendly to indicate updated parameters.

The rationale for using power spectrum analysis over analyzing the amplitude and frequency of preBötC activity is unclear. The physiological relevance of power in higher harmonic frequencies should be explained.

When discussing TRPM4 and ICAN, Picardo et al., 2019 PLOS Biology should be cited and discussed.

Reviewer #3 (Recommendations for the authors):

The manuscript is well-written and clear. The experiments are appropriate to test the hypotheses and the data is convincing. This manuscript is significant because it provides substantive evidence for the role of INaP in modulating breathing frequency and ICAN in altering amplitude with some interesting boundary conditions when ICAN and INaP are selectively blocked. Of particular value is the addition of a channelrhodopsin current (based on a Markov formalism) to the authors' previously published model.

I have no major concerns regarding the manuscript.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Predictions and experimental tests of a new biophysical model of the mammalian respiratory oscillator" for further consideration by eLife. Your revised article has been evaluated by Ronald Calabrese (Senior and Reviewing Editor).

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Please revise according to the reviewer Recommendations to the authors. Re-review will be by the reviewing editor.

Reviewer #1 (Recommendations for the authors):

The authors have adequately addressed all my comments and I appreciate the effort made to better describe this nice work to the broader readership of eLife. I congratulate the authors for their work.

Reviewer #2 (Recommendations for the authors):

In this revised manuscript, Phillips et al., respond to many of the reviewers’ concerns; however, there remain a few issues that should be addressed.

From Essential Revisions

1. Regarding limitations of the ChR2 experiments, the authors should mention and discuss the possibility that optogenetic stimulation of glutamatergic terminals may synaptically activate preBötC inhibitory neurons, thus altering excitation-inhibition balance (Ashhad and Feldman 2020). Could this mechanism also explain the post-stimulus inhibition?

2. At the end of the Discussion, in the Summary, and in the author’s response, the authors state that their results support the statement: “INaP is essential for rhythm generation in the reduced in vitro preparation used in this study.” A similar qualifier, like adding “in vitro”, should be placed wherever a statement about InaP being essential is made, especially in the abstract, second to last paragraph of Introduction, and first two paragraphs of the Discussion.

Reviewer #3 (Recommendations for the authors):

The authors have addressed the majority of my comments. My only remaining concern is their unwillingness to assess variability in their data since this seems a trivial “ask”---particularly if they choose perhaps the simplest metric of variability, coefficient of variation. Nonetheless, I still feel the manuscript is of value and advances the field and the authors have addressed the majority of concerns for each of the reviewers.
