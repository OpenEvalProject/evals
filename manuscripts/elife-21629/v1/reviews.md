# Peer review - Round 1

Editors:
- Liqun Luo, Howard Hughes Medical Institute, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.21629.032](https://doi.org/10.7554/eLife.21629.032)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Calcium dynamics regulating the timing of decision-making in C. elegans" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Eve Marder as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you see from the attached reviews, all reviewers find your study of interest, but raised a number of critiques ranging from genetics to modeling. We hope that you will be able to address these critiques in a revised manuscript in the next few months. You should scale back your molecular-level conclusions where evidence is not definitive. We look forward to receiving your revised manuscript.

Reviewer #2:

In this study Tanimoto et al. address how sensory information is encoded by neurons to implement behavioral decisions. The authors developed new experimental setups and using these approaches provide an interesting conceptual framework linking sensory neural activity to behavior. More specifically, based on their behavioral data they propose a novel negative chemotaxis strategy during which animals accumulate sensory evidence prior to a behavioral decision, switching from a pirouette to a forward-run behavioral state. By calcium imaging they show that AWB chemosensory neuron responses, in contrast to ASH nociceptive neurons, can be fitted to a leaky-integrator model, which could be an essential feature of the evidence-accumulation mechanism. They substantiate this finding with a computer simulation of chemotaxis.

Investigating the molecular basis for the temporal integration of olfactory stimuli in AWB, they first confirm that the integration is a cell autonomous property of AWB. They then show that the odr-3 Ga protein is essential for the response property of the neurons.

Furthermore, they show that the calcium accumulation in AWB and ASH can be attributed to L-type Ca VG calcium channels, and not to B-type, thought there must be other components in ASH, as only the late response phase is affected.

This manuscript could present both a technical and conceptual advance showing for the first time that evidence accumulation for decision making can be performed by a single sensory neuron class, including an underlying molecular mechanism, as opposed to circuit mechanisms proposed by work in higher animals. However, I think not all conclusions are sufficiently supported in the present form and some experiments need more repetitions and appropriate statistical tests.

The manuscript is well written and easy to follow with some exceptions that should be addressed in a revised manuscript (see below); the graphs are clear, supplemental data are appropriately provided.

Major comments

1) Experiments in Figures 1–2 are performed in a closed loop configuration, i.e. movement directly feeds back onto sensory input. This is not the case for the open loop virtual gradient setup in subsequent experiments. This difference should be better addressed in the discussion text.

2) Figure 4A,B and E. I am not convinced that AWB and ASH sensory response profiles could not be fitted equally well to the alternative model in each panel. The authors should provide goodness of fit results for all models on each neuron dataset and perform appropriate statistical tests showing that one model performs significantly better than the corresponding null hypothesis model.

3) The authors use a threshold to determine when sensory information leads to an abrupt change in turning frequency. It is not sufficiently explained how exactly this 99%-prediction-interval is calculated. Provide more information in main text about the logic and details in Materials and methods section.

4) I am not convinced that the turning rate profiles in Figure 4A–B middle and right panels show discrete transitions. In Figure 4A-middle panel this is only supported by one data point (arrow). Otherwise, like in the right panel the trace increases gradually; but this is very difficult to judge because of the variability. Same in 4B-middle+right panels. The traces are gradually declining already prior to the onset of the odor down ramp. Moreover, the rates in 4A and 4B right panels are not found to remain consistently above/ below the threshold. I think these experiments require more repetitions, statistics and a no-odor-ramp control of the same larger dataset size. Otherwise the major conclusions of the paper are not sufficiently supported.

5) The differentiation between "reflex" and temporally delayed decision in up versus down ramp is not well founded in the given data. In fact, both responses in 4A vs 4B show very similar profiles, just with opposite signs. The difference is made mainly by the chosen thresholds.

6) The direct functional role of sensory information encoding in directional choice (as stated in the first sentence of the Discussion) is in fact never established due to the open loop configuration. This conclusion should be toned down.

Reviewer #3:

In this study the authors investigate the neural mechanisms underlying nonanone avoidance in C. elegans. Using behavioral tracking experiments, they find that, as previously shown for other types of worm chemotaxis, animals show a higher rate of turning when traveling in the aversive direction (here, toward higher repellent concentrations). In addition (and in contrast to salt chemotaxis), the authors find that following these reorientations the angle of bearing is biased away from the source of repellent. Through calcium imaging experiments, they correlate the increase in turn probability with the ASH sensory neurons, which show a rapid on response to nonanone increases, and the bias in run direction to the AWB neurons, which show a slow, "leaky integrator" off response to nonanone decreases. Finally, they analyze a number of signaling and ion channel mutants to explain molecular basis of these differing neural responses.

In general, this is a very interesting paper. The behavioral analysis and subsequent calcium imaging from the respective sensory neurons provides a satisfying explanation for the behavioral strategy underlying aversive chemotaxis and its basic neural mechanism. However, I had a number of questions/concerns regarding the genetic experiments investigating the roles of particular calcium channels in sensory neuron dynamics, and found some of the conclusions here to be overstated. Specifically:

1) The genotypes in all the genetic experiments are poorly and incompletely documented. For example, the alleles used for egl-19, unc-68, unc-2, and itr-1 are not stated (at least I couldn't find them) and it is not stated how many times the strains were backcrossed.

2) From what I can tell, the authors only analyzed a single allele of each gene in question, and did not test whether any were rescued cell-specifically in the cells whose activity was measured. Since most of these genes are pan-neuronal or otherwise broadly expressed in the nervous system, it is not possible to reliably infer that they are functioning cell-autonomously in a particular neuron. Moreover, by only testing a single allele and not testing for rescue, it is not possible to even be sure the effect is due to the gene of interest as opposed to something else in the background.

3) Regarding the calcium channel mutants, the results in ASH are hard to reconcile with the results of Zarhatka et al., 2015. These authors showed that NemA completely blocked cell body calcium transients in ASH in response to a different odorant, octanol. Since presumably both octanol and nonanone are sensed in the cilium, it is hard to explain how the responses they induce could be conveyed to the cell body through different voltage-sensitive channels. Do the authors also see only a partial reduction in octanol response in their system? Is the fast initial response affected by the other (untested) VGCC gene cca-1? Also, the effect of the egl-19 reduction of function mutation is not shown in the figure. How does egl-19(lf) compare quantitatively with the supposedly complete block caused by NemA? Obviously it is not necessary for the authors' nonanone results to match Zarhatka's octanol results, but the differences are striking enough to merit further investigation.

4) I also thought the authors slightly overinterpreted the odr-3 results. odr-3 is expressed in many olfactory neurons besides AWB, so without cell-specific rescue it is a leap to infer cell-autonomy. Moreover, odr-3 mutants have been reported by Bargmann et al. to have abnormal cilium structure, so its effect may be of a developmental rather than a signaling nature. More generally, the nature of olfactory G-protein signaling is not well-understood in any C. elegans neuron, so inferring a specific role in signal integration on the basis of a single, unrescued allele (and without understanding the signaling basis of the primary response) seems problematic.

In summary, I really like the first part of the paper, but I think the mutant analysis at the end would require a lot of additional genetic experiments (multiple alleles, cell-specific rescue, perhaps testing other candidates like cca-1 and gpa-6) to justify the authors' conclusions. I think it is probably beyond the scope of this paper to do all these extra experiments, so I would instead recommend the authors correct the most important omissions and otherwise scale back their molecular conclusions. Such a paper would still be a very interesting study.

Reviewer #4:

Tanimoto et al. use the well-defined C. elegans chemosensory system to probe the relationship between neural activity patterns and behavior. They combine optogenetics with calcium imaging and behavioral analysis show that ASH and AWB sensory neurons use two different strategies to encode odor information. They also link different calcium channels with these two strategies. Importantly, they claim that the different strategies might explain decision making in behavior. There are some interesting data here, but I feel that some of it has been over interpreted. I do think with some changes, this should be a very interesting story.

Major comments

1) What are the differences between "bearing at run initiation" and "bearing after a turn"? Does "bearing after a turn" include the turn with the pirouette? It would be nice to see an example trace to recognize these differences clearly.

2) I believe the authors generated panel Figure 2D by comparing dC/dt in 1 sec window to p(turn) in the two different behavioral phases. They then state 'the efficient transitions between discrete behavioral states based on odor concentration information…'. This quote, along with the surrounding text, seems to imply that odor concentration drives the behavioral transition. Although this is likely true, I see no evidence for it here. For instance, let us consider a worm model in which the worm randomly transitions to a high turning mode (one that is insensitive to C). In this model, the worm would still behave differently at every dC/dt value. Although this model may be silly, it demonstrates that there are models that comply with panel D in which dC/dt does not drive behavioral transitions.

3) I don't understand why the authors used two different types of models for 4A and 4B. The AWB model looks like a more biologically realistic model (at least, it's a standard model). I'm pretty sure the AWB model could be fit to both ASH and AWB. For instance, if we use (1/tau) dx/dt = a*dC/dt – b*x(t), we should be able to use a faster time constant to produce ASH (https://www.wolframalpha.com/input/?i=dx%2Fdt+=+1+-+.1*x) and a slower time constant to produce AWB (https://www.wolframalpha.com/input/?i=10*dx%2Fdt+=+1+-+.1*x). I think it is important to use the same (more biologically relevant) model for both neurons if possible. While this might be beyond the scope, an even more realistic model would probably be: (1/tau) dx/dt = a*f(C) – b*x(t) where f is a function representing receptor saturation.

4) It would be nice if the authors clearly label 'contribution of AWB', etc. in panel 5A. Also, the authors find that the 'time-integral' model produces a more robust/accurate behavior (C). This might give more credence to fitting 'time-integral' models to both AWB and ASH (see comments for F4).

5) The authors used unc-13, but I would also recommend using unc-31 to test whether that this might affect the time delay in AWB.

6) Odr-3 results are a bit confusing. Given that the nonanone receptor has not been identified, do the authors claim that odr-3 is coupling to this unknown receptor(s). Or is the property of AWB and ASH modified in an odr-3 loss of function.

7) I would also recommend using cell-specific knockouts of the calcium channels, which would allow the authors to isolate the effect to the neurons being analyzed.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Calcium dynamics regulating the timing of decision-making in C. elegans" for further consideration at eLife. Your revised article has been favorably evaluated by Eve Marder (Senior editor), a Reviewing editor, and three reviewers.

The manuscript has been improved but before final acceptance, we would like you to address the relatively minor issues raised by Reviewer #2 and Reviewer #4 below.

Reviewer #2:

In the revised version the authors made a good effort to address my concerns. Besides providing additional repetitions for some of their experiments, I requested convincing statistical tests that show whether ASH and AWB imaging data indeed can be better fitted to either one of the models. After their revisions, I am convinced that this is the case for AWB data, which indeed are better explained by the leaky integrator equation. The ASH fitting data however are less convincing. But I agree with the authors that ASH response profiles might be better represented by the time differential during the onset of the response. I think the authors do an appropriate job in addressing this weakness of the study in their discussion, but why leaving future readers with a question mark until they make it to this point. Therefore, I recommend they should give a bit more emphasis on explaining the rather poor fit results for ASH already in the Results section. Allover, I think this paper is a tour de force involving sophisticated technology and analyses. The results are very interesting and provide a working hypothesis for exciting future studies.

Reviewer #3:

I think the authors have done a good job addressing previous reviewer comments. It is an interesting study, and I am happy to recommend publication.

Reviewer #4:

I am satisfied with this version and the authors efforts to address the reviewer's comments.

One additional thing would be to add "saturation of the input" to the standard biophysical model. They could do this by putting the input through a logistic sigmoid or something similar. While this would be nice, it is not essential.

I recommend accepting the manuscript for publication.
