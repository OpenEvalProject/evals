# Peer review - Round 1

Editors:
- Anna C Schapiro, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76384.sa0](https://doi.org/10.7554/eLife.76384.sa0)

This paper presents a generative adversarial network-inspired model of how learning during wakefulness, non-rapid eye movement (NREM), and REM sleep work together to facilitate the emergence of object category representations. The model is impressive in its ability to shape representations based on internally generated activity that does not directly recapitulate prior experience, and has properties that correspond to replay and dreams in NREM and REM sleep. The model makes predictions that can be tested in sleep experiments in humans and animals.


---

# Peer review - Round 1

Editors:
- Anna C Schapiro, https://ror.org/00b30xv10 University of Pennsylvania United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76384.sa1](https://doi.org/10.7554/eLife.76384.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Memory semantization through perturbed and adversarial dreaming" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Blake A Richards (Reviewer #2); Ari Benjamin (Reviewer #3).

After consultation with the reviewers, we have decided on a rejection of the current manuscript with the possibility of resubmission of a substantially revised new manuscript. All reviewers felt that the model was interesting and impressive. The main issues that led us to this decision were a use of semanticization that seemed too different from its use in the cognitive neuroscience literature, making it unclear how to align the model and its predictions with the empirical literature, and lack of theory or analysis to make it clear why the model works. We felt that a version of the paper that addressed these points would essentially be a new paper, as it involves restructuring the framing and discussion, a new title, and substantial new analysis/theory. This comment from Reviewer 3 is the crux of the theory issue: "If the objective of GANs and VAEs are themselves insufficient for representation learning, absent architecture, why would their combination here avoid that problem? " If you decide to resubmit to eLife, the paper will likely go back to the same editors and reviewers.

Reviewer #1:

This paper presents a model inspired by generative adversarial networks that shows how different forms of nonveridical generative replay can lead to meaningful changes in representations. The authors simulated three cycling states––wakeful learning, NREM sleep, and REM sleep––as optimizing different learning objectives. The model consists of a feedforward pathway that learns to map low–level sensory inputs to high–level latent representations and to discriminate between external stimuli and internally simulated activity, and a feedback pathway that learns to reconstruct low–level patterns from high–level representations. During wakefulness, the model learns to reconstruct the sensory inputs it receives, while storing their associated latent vectors into a memory buffer representing the hippocampus. During NREM, low–level patterns are generated from individual memory traces in the hippocampus. The feedforward pathway processes occluded versions of these patterns and learns to reconstruct the original memory traces. In REM, patterns are generated based on random combinations of hippocampal memories. The feedforward pathway learns to avoid labeling these patterns as external inputs and the feedback pathway tries to trick the feedforward pathway into recognizing them as external stimuli. After training with several cycles of these three learning phases on naturalistic images, the model develops more linearly separable latent representations for different categories, which the authors interpret as evidence for semanticization.

There are several aspects of this model that are very interesting and impressive. It is able to reorganize internal memory representations in a meaningful way based only on internally generated activity. The demonstrations that occlusions in NREM work best on single episodes and that REM works best when using combined episodes have an intriguing correspondence to known properties of replay and dreams in these sleep stages. As detailed below, there are other aspects of the model that seem less consistent with known properties of sleep, and it is unclear whether the performance metrics demonstrate "semanticization" as the term is typically used in the literature.

1. One aspect of the model that stands out as being in tension with neural data is that cortical activity during REM is known to be less driven by the hippocampus than during NREM, due to fluctuations in acetylcholine. In the model, the hippocampus is the driver of replay throughout the model in both states.

2. The model predicts that internally generated patterns should become more similar to actual inputs over time, but REM dreams appear to be persistently bizarre, and in rodents there seems to be a decrease in veridical NREM replay over time after a new experience.

3. The use of linear separability as an index of semanticization seems in tension with the literature on semantics in a few ways. Areas of visual cortex that are responsive to certain categories of objects are not typically thought to be processing the semantic structure of those objects, in the way that higher level areas (e.g. anterior temporal lobes) do. Semanticization has the connotation of stripping episodes of their details and source information and representing the structure across experiences within the relevant domain, often in a modality–independent way. It is not clear that a simple separation between visual categories captures these senses of the word.

4. It is unclear when the predictions of the model apply to a night of sleep vs. several nights vs. hundreds or thousands (a developmental timescale). For example, the authors propose depriving subjects of REM sleep and testing the ability to form false memories. Putting aside the difficulty of REM deprivation, it is unclear how many nights of deprivation would be required to test the predictions of the model, especially because REM does not seem to be beneficial during the first few learning epochs (Figure 4).

Recommendations for the authors

1. McClelland, McNaughton, and O'Reilly 1995 is cited as a standard consolidation theory, but it belongs in the transformation theory category. The hippocampal memories in that model do not tend to retain their episodic character when consolidated in neocortex.

2. Norman, Newman, and Perotte 2005, Neural Networks, had a neural network model of REM that deserves discussion here.

3. The authors might consider simulations demonstrating to what extent alternation between sleep stages is needed and simulations demonstrating whether the order of replay matters – does the model behave differently if REM precedes NREM?

4. My understanding is that for analyses in Figure 5 the test dataset consists of occluded versions of training images. Does linear separability increase for occluded versions of images that are not presented during training?

5. Memories are linearly combined to guide reconstruction during REM. It could be useful to demonstrate that this does better than random activity patterns (patterns not based on memories).

Reviewer #2:

In this paper, Deperrois et al. develop a neural network model of unsupervised learning that uses three distinct training phases, corresponding to wakefulness, NREM sleep, and REM sleep. These phases are respectively, used to train for reconstructing inputs (and recognizing them as real), representing perturbed sensory inputs similar to non–perturbed sensory inputs, and recognizing internally generated inputs created from mixing stored memories. They show that this model can learn decent semantic concepts that are robust to perturbations, and they use ablation studies to examine the contribution of each phase to these abilities.

Overall, I really enjoyed this paper and I think it is fantastic. Its major strengths are its originality, its clarity, and its well–designed ablation studies. The authors have developed a model unlike any other in this area, and they have given the reader sufficient data to understand its design and how it works. I believe this paper will be important for researchers in the area of memory consolidation to consider. Moreover, the model makes interesting empirical predictions that can and should be tested.

The weaknesses of the paper are as follows:

1) It is odd that eliminating the NREM phase didn't have much of an impact on the accuracy for non–occluded images (Figure 5). My guess: classification on non–occluded images would drop more with the removal of NREM if the authors had used more perturbations than just occlusion, e.g. like those used in SimCLR. Though these additional experiments do not need to be included for the paper to be publishable, per se, I do think they should be considered by the authors (or other researchers) for future studies. This is particularly so because, as it stands, the results suggest that the NREM phase is merely helping the system to be better at recognizing occluded images, which is a wee bit trivial/obvious given that the NREM phase is literally training on occluded images. All that being said, Figure 6e seems to suggest that NREM does help with separating inter–class distances. So, I am left a little confused as to what the actual result is on this matter. The authors only discuss these issues briefly on lines 393–397, and this really could be expanded.

2) I do not see any reason to run z through the linear classifier weights before performing t–SNE. Moreover, I am concerned that this ends up just being equivalent to an alternative means of visualizing classification accuracy. First, t–SNE should be able to identify these clusters from z itself, and there is essentially no logic provided as to why it wouldn't be able to do this–after all, this is what t–SNE was designed to do. Second, the linear projection of z with the classifier weight will necessarily correspond to a projection of the z vectors that increases the separation between classes. So, really, what we're visualizing here is how well that linear projection separates the classes. But that is already measured by classification accuracy. As such, I don't see what this analysis does beyond the existing data on classification accuracy. I think the authors should have performed t–SNE on the z vectors directly. If the authors are determined not to do this, they should provide much better logic explaining why this is not an appropriate analysis. To reiterate: t–SNE is designed for this purpose and has been used like this in many other publications!

3) In the discussion on potential mechanisms for implementing the credit assignment proposed here, the authors only mention one potential solution when there are literally dozens of papers on biologically realistic credit assignment in recent years. Lillicrap et al. (2020) and Whittington and Bogacz (2019) both provide reviews of these papers. Plus, Payeur et al. (2021) provide an exhaustive table in their supplementary material listing the different solutions on offer and their properties. The authors should note that there are a multitude of potential solutions, not just one, and reference at least some of these.

Recommendations for the authors

1) It is probably worth noting/mentioning that most people report having dreams with completely novel/surreal elements that can be wholly different from their past experiences (e.g. flying), suggesting that not all dreams are a result of rearranging fragments from stored episodic memories. The authors should discuss this and recognize it as a potential limitation of the model.

2) The perturbed dreaming phase is highly reminiscent of existing self–supervised models from machine learning (e.g. SimCLR, BarlowTwins, etc.), since it is essentially training the feedforward network to match perturbed/transformed versions of the same images to the same latent state as each other. For sake of providing the reader with more intuition about what is happening in the model, the authors should expand the discussion of these links.

3) A few typos to fix:

– Line 30: organisms –> organism's

– Line 47: sleep state –> sleep states

– Line 341: Our NREM phase does not require to store raw sensory inputs… –> Our NREM phase does not require the storage of raw sensory inputs…

4) Figure 6e and f are confusing and need to be improved. First, it is unclear what the two different bars for each training regime represent. Second, the y–axes don't make it clear that this is the ratio of intra–to–inter class distances, and the legend has to be referred to for that, which is not helpful for clarity.

5) To be completely candid with the authors, Figure 7b is very confusing and not terribly helpful for the reader. I understand that this is a sketch of the authors' current thinking on how their PAD model could relate to cortical circuits, but making concrete sense of exactly what is being proposed is nigh impossible. I think the authors should consider removing this panel and simply noting in the text that there are potential biological mechanisms to make the PAD model feasible. As it stands, Figure 7b takes a strong, clear paper and ends it on a very confusing note…

6) In equation 1, are all three losses really weighted equally over all of training? I'm surprised that the KLD term isn't given a schedule. This is common with VAE models and can help with training.

7) In section 4.4.4 and 4.4.5 the numbers use a single quote to denote the thousands decimal, but that's a mistake: it should be a comma, e.g. 10,000 not 10'000.

8) Figure 10 and section 6.1: L_latent is never defined. What is it? Is that what equation 12 was supposed to define (which would make sense, given that equation 2 already defined L_img). Also, why does it increase during training? Similarly, L_fake is never defined.

Reviewer #3:

The proposal that the brain learns adversarially during sleep stages is fascinating. The authors propose that not only does feedback to the earliest areas form a generative model of those areas, but that also feedforward activity carries the dual interpretation of a discriminator. (This proposal aligns with that of Gershman (2019) https://www.frontiersin.org/articles/10.3389/frai.2019.00018/, which should be cited here). If it could be shown that this is indeed what the brain does the impact would be tremendous. However, the evidence presented in the manuscript does not yet make a strong case.

The paper focuses primarily on modeling semantization, and this is defined as the degree to which object categories can be linearly decoded from the top layer of an encoding/decoding neural network. It is worth noting that other communities might call this a model of 'unsupervised representation learning' rather than semantization during memory consolidation. But is linear decodability of object categories an equivalent concept to the semantization of episodic memory? This seems to miss much about memory consolidation.

The focus on decodability is also problematic in part because it's not clear what about the model leads to it. In the ML community, it is known that the objectives of generative modeling and autoencoding are by themselves insufficient to provide "good" representations measured by linear decodability of supervised labels. (For arguments why, see https://arxiv.org/pdf/1711.00464.pdf and https://arxiv.org/abs/1907.13625 for autoencoders and https://www.inference.vc/maximum–likelihood–for–representation–learning–2/ for GANs). If such a system empirically learns untangled representations of categories, it is because the network architecture or prior distribution over latents is constraining in some way. The authors claim that "generating new, virtual sensory inputs via adversarial dreaming during REM sleep is essential for extracting semantic concepts" (line 14–15, also 221–222). If the objective of GANs and VAEs are themselves insufficient for representation learning, absent architecture, why would their combination here avoid that problem? For example, is the DCGAN–like architecture crucial? This is possible, but only one architecture was tested. (It is also concerning that the linear decodability of representations in DCGANs can be much higher than reported here; some component of the model is deteriorating, rather than giving, this quality. See Radford et al. (2014)). What about the REM stage in particular is necessary – for example, does it work when randomly sampling from the prior over Z or just convex combinations? Overall, from the computational perspective, I don't think it is yet supported that this objective function necessarily leads to learning untangled, semantic representations from which labels are linearly decodable.

Linear decoding aside, is this a good model of neural physiology and plasticity? It's a promising direction, and I like the discussion of NREM and REM. However, for a model this radical to be convincing I think much more attention should be paid to what this would look like biologically. Some specific questions stand out:

– I find it concerning that the generative model is only over the low–level inputs, e.g. V1 (or do the authors believe it would be primary thalamus?). In the predictive processing literature, it is generally assumed that *at every layer* feedback forms an effective generative model of that layer. In the hierarchical model here, there is no relation between the intermediate activations in the feedforward path to those in the feedback path. This prevents the integration of top–down information in intermediate sensory areas and makes the model unrealistic.

– What neurobiological system do the authors propose implements the output discriminator? If there are no obvious candidates, what would it look like, and what sorts of experiments could identify it?

– What consequences would the re–use of the feedforward model as a discriminator have for sensory physiology? This is a rather radical change to traditional models of forward sensory processing.

– The proposed experiments would test if sleep stages are involved in learning, but wouldn't implicate any adversarial learning. For example, the proposal to interrupt REM sleep would not dissociate this proposal from any other in which REM sleep is involved in sensory learning.

– I think an article modeling consolidation should be situated in hippocampal modeling. Yet here the hippocampus is modeled simply as a RAM memory bank, and the bulk of modeling decisions are about cortical perceptual streams. If the proposal is that this is what the hippocampus effectively does, it would be nice to have a mechanistic discussion as to how the hippocampus might linearly interpolate between two memory traces during the NREM stage. In general, what would this predict a hippocampal physiologist would see?

– Many related algorithms are dismissed in lines 380–381. I'm not sure what optimization tricks have been removed. Perhaps the authors could explain what was removed and why this makes PAD biologically plausible. In my opinion many of these are comparable.

I love the originality of this work. Yet to be taken seriously I think it needs to be much more firmly rooted in experimental findings and predictions. A review/perspective format with demonstrative simulations could be more appropriate.

In my opinion the focus on semantization/ linear decodability is a cherry on top of the main proposal, which is the adversarial framework for sleep stages. Given my reservations about the decodability aspects I think it may be a stronger paper if the framing shifts to focus on sleep physiology and unsupervised learning.

Miscellaneous comments.

– Is it spelled semantization or semanticization? The latter appears to be in more common use.

– I found the tSNE plots not particularly useful. tSNE is nonlinear so it is not a measure of linear category untangling. Please say more about what exactly this measure means, and report the perplexity parameter and how it was chosen.

– The authors should be aware of recent failures to replicate the Berkes (2011) result: https://elifesciences.org/articles/61942

Finally, some citations that I think could be mentioned:

Previous proposals that the brain may learn adversarially:

– Gershman, Samuel J. "The generative adversarial brain." Frontiers in Artificial Intelligence 2 (2019): 18.

– https://arxiv.org/abs/2006.10811 (full disclosure, a work of my own)

Work in the ML community in which the encoder is also a discriminator:

– Brock, Andrew, Lim, Theodore, Ritchie, James M, and Weston, Nick. Neural photo editing with introspective adversarial networks. arXiv preprint arXiv:1609.07093, 2016.

– Ulyanov, Dmitry, Vedaldi, Andrea, and Lempitsky, Victor. It takes (only) two: Adversarial generatorencoder networks. In Thirty–Second AAAI Conference on Artificial Intelligence, 2018.

– Huang, Huaibo, He, Ran, Sun, Zhenan, Tan, Tieniu, et al. Introvae: Introspective variational autoencoders for photographic image synthesis. In Advances in neural information processing systems, pp. 52–63, 2018.

– Munjal, Prateek, Paul, Akanksha, and Krishnan, Narayanan C. Implicit discriminator in variational autoencoder. arXiv preprint arXiv:1909.13062, 2019.

– Bang, Duhyeon, Kang, Seoungyoon, and Shim, Hyunjung. Discriminator feature–based inference by recycling the discriminator of gans. International Journal of Computer Vision, pp. 1–23, 2020.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Learning cortical representations through perturbed and adversarial dreaming" for further consideration by eLife. Your revised article has been evaluated by the same three reviewers.

The manuscript has been improved and the reviewers were overall positive, but they have one significant remaining request and one minor request for a caveat:

The significant request is to expand on how exactly the theory can be tested in experiments, with particular emphasis on diagnostic experiments that would allow us to rule out plausible alternatives. From Reviewer 3: "It takes a lot of thought to imagine how this particular hypothesis would surface in data and I don't think it should be left to the reader. More specifically, the paper still has no experimental predictions that could separate this idea from other similar possibilities involving generative models. The authors agreed in the response that they pose few predictions for the adversarial component, and instead only for "whether REM sleep is involved in cortical representation learning using a generative model." The anterior prefrontal cortex is now briefly mentioned as the top of the discriminator, but surely there would be a great deal of evidence in connectivity, power over plasticity, lesion studies, etc., that could confirm this. Re: "we interpret the reported novelty of REM dreams as strong existing evidence that this learning is based on adversarial principles rather than driven by reconstructions," (531-533): Here I disagree (though yes, not reconstructions). It is a strong hint that it is driven by an offline stage involving generative processes. This need not be adversarial. The Wake-Sleep algorithm, for example, also has a Sleep phase in which the hierarchical generative model generates samples via ancestral sampling from the top-level prior distribution. (Perhaps there is a misunderstanding regarding WS: the introduction currently dismisses the WS algorithm with the sentence, "these models explicitly try to reconstruct observed sensory inputs, while most dreams observed during REM sleep rarely reproduce past sensory experiences", lines 40-41. WS does try to reconstruct inputs during wake, but during sleep it 'fantasizes' randomly like a GAN.) Thus I still feel the paper does not offer tests by which we could know if the model were true."

The minor request is to acknowledge in the intro and the new discussion paragraph that the generative algorithm likely requires certain architectures & priors to deliver semantic representations.

Typo: "Moreover, removing NREM from training also increases [this] ratio." .
