# Peer review - Round 1

Editors:
- Marius V Peelen, Radboud University Nijmegen Netherlands

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.94191.3.sa0](https://doi.org/10.7554/eLife.94191.3.sa0)

This paper provides valuable insights into the neural substrates of human working memory. Through clever experimental design and rigorous analyses, the paper provides compelling evidence that the working memory representation of stimulus orientation is a reformatted version of the presented stimulus, though more work is needed to establish more generally that visual working memories are abstractions of percepts. This work will be of broad interest to cognitive neuroscientists working on the neural bases of visual perception and memory.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94191.3.sa1](https://doi.org/10.7554/eLife.94191.3.sa1)

Summary:

The authors aim to test the sensory recruitment theory of visual memory, which assumes that visual sensory areas are recruited for working memory and that these sensory areas represent visual memories in a similar fashion to how perceptual inputs are represented. To test the overlap between working memory (WM) and perception, the authors use coarse stimulus (aperture) biases that are known to account for (some) orientation decoding in visual cortex (i.e., stimulus energy is higher for parts of an image where a grating orientation is perpendicular to an aperture edge, and stimulus energy drives decoding). Specifically, the authors show gratings (with a given "carrier" orientation) behind two different apertures: One is a radial modulator (with maximal energy aligned with the carrier orientation) and the other an angular modulator (with maximal energy orthogonal to the carrier orientation). When subject detect contrast changes in these stimuli (the perceptual task), orientation decoding only works when training and testing within each modulator, but not across modulators, showing the impact of stimulus energy on decoding performance. Instead, when subjects remember the orientation over a 12s delay, orientation decoding works irrespective of the modulator used. The authors conclude that representations during WM are therefore not "sensory-like", given that they are immune to aperture biases. This invalidates the sensory recruitment hypothesis, or at least the part assuming that when sensory areas that are recruited during WM, they are recruited in a manner that resembles how these areas are used during perception.

Strengths:

Duan and Curtis very convincingly show that aperture effects that are present during perception, do not appear to be present during the working memory delay. Especially when the debate about "why can we decode orientations from human visual cortex" was in full swing, many may have quietly assumed this to be true (e.g., "the memory delay has no stimuli, and ergo no stimulus aperture effects"), but it is definitely not self-evident and nobody ever thought to test it directly until now. In addition to the clear absence of aperture effects during the delay, Duan and Curtis also show that when stimulus energy aligns with the carrier orientation, cross-generalization between perception and memory does work (which could explain why perception-to-memory cross decoding also works). All in all, this is a clever manipulation, and I'm glad someone did it, and did it well.

Weaknesses:

There seems to be a major possible confound that prohibits strong conclusions about "abstractions" into "line-like" representation, which is spatial attention. What if subjects simply attend the end points of the carrier grating, or attend to the edge of the screen where the carrier orientation "intersects" in order to do the task? This may also result in reconstructions that have higher bold at areas close to the stimulus/screen edges along the carrier orientation. The question then would be if this is truly an "abstracted representation", or if subjects are merely using spatial attention to do the task.

Alternatively (and this reaches back to the "fine vs coarse" debate), another argument could be that during memory, what we are decoding is indeed fine-scale inhomogenous sampling of orientation preferences across many voxels. This is clearly not the most convincing argument, as the spatial reconstructions (e.g., Figure 3A and C) show higher BOLD for voxels with receptive fields that are aligned to the remembered orientation (which is in itself a form of coarse scale bias), but could still play a role.

To conclude that the spatial reconstruction from the data indeed comes from a line-like representation, you'd need to generate modeled reconstructions of all possible stimuli and representations. Yes, Figure 4 shows that a line results in a modeled spatial map that resembles the WM data, but many other stimuli might too, and some may better match the data. For example, the alternative hypothesis (attention to grating endpoints) may very well lead to a very comparable model output to the one from a line. But testing this would not suffice, as there may be an inherent inverse problem (with multiple stimuli that can lead to the same visual field model).

The main conclusion, and title of the paper, that visual working memories are abstractions of percepts, is therefore not supported. Subjects could be using spatial attention, for example. Furthermore, even if it is true that gratings are abstracted into lines, this form of abstraction would not generalize to any non-spatial feature (e.g., color cannot become a line, contrast cannot become a line, etc.), which means it has limited explanatory power.

Additional context:

The working memory and perception tasks are rather different. In this case, the perception task does not require the subject to process the carrier orientation (which is largely occluded, and possibly not that obvious without paying attention to it), but attention is paid to contrast. In this scenario, stimulus energy may dominate the signal. In the WM task, subjects have to work out what orientation is shown to do the task. Given that the sensory stimulus in both tasks is brief (1.5s during memory encoding, and 2.5s total in the perceptual task), it would be interesting to look at decoding (and reconstructions) for the WM stimulus epoch. If abstraction (into a line) happens in working memory, then this perceptual part of the task should still be susceptible to aperture biases. It allows the authors to show that it is indeed during memory (and not merely the task or attentional state of the subject) that abstraction occurs.

What's also interesting is what happens in the passive perceptual condition, and the fact that spatial reconstructions for areas beyond V1 and V2 (i.e., V3, V3AB, and IPS0-1) align with (implied) grating endpoints, even when an angular modulator is used (Figure 3C). Are these areas also "abstracting" the stimulus (in a line-like format)?

Review after revision:

(1) It's nice of the authors to simulate how a dot stimulus affects the image computable model, but this does not entirely address my concern about attention to endpoints. The assumption that attention can be used in the same manner as a physical stimulus to calculate stimulus energy is questionable. (also, why would a dot at 15º lead to high stimulus energy tangential to that orientation?). This simulation also does not at all address my concern about model mimicry (many possible inputs can lead to a line-like output).

(2) It's also nice that the authors agree that much more work needs to be done, and these results may not generalize to all forms of memory. Given this agreement, and until that "more work" is done, I strongly believe we should refrain from making hyperbolic claims that might preemptively imply all visual working memories are abstractions of percepts. Time (and much more work) will likely show things to be much more subtle and complex.

The work presented in this paper is cool, but it uses a specific case: spatial stimuli (gratings) with the task to remember orientation. This limits possible conclusions for several reasons (1) These results are specific to EVC, as visual maps are a prerequisite meaning that these results will not hold up in other, non-retinotopic areas. (2) The fact that subjects are "focusing" along the main stimulus axis (attention or not) can simply be a strategy employed by the majority of (but not all) subjects - a strategy that may not be necessary to do the task, and therefore not a canonical method of Abstraction. It may be a "shared preferred strategy" or something. (3) If subjects had to (for example) remember contrast, and not orientation, results may have been entirely different (I would hypothesize there is no line-like abstraction in this case). Vice versa, if the perceptual task would have been on orientation (instead of contrast), the authors admit that "participants would reformat the grating into a line-like representation to make the judgments" (quote from author's response under "Additional context"). Thus, the results may be entirely about the task/ cognitive state, and not about how perceptual information is abstracted into memory.

Instead of unveiling *the* working memory Abstraction, this work (very nicely) shows a specific instance of possible abstraction. A more correct (but admittedly, less "sexy") conclusion may be "Visual working memories of orientation can be abstracted into a line in early visual cortex". As it stands, the authors still do not acknowledge any of the alternatives that myself (see above) and the other reviewers have put forth, nor do they acknowledge recent work by Chunharas et al. (2023, BioRxiv), that directly applies principles of efficient coding to address the exact same question of working memory abstraction. The link between a "line-like" representation and efficient coding implied by the authors (in their response) is merely tentative to me, but it would be great if the authors could explain this further.

These were, and remain, the major weaknesses in the original submission, that in my view have not been adequately addressed by the authors, as many overly broad conclusions about abstractions are currently still present in the manuscript (in for example the title).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.94191.3.sa2](https://doi.org/10.7554/eLife.94191.3.sa2)

Summary:

In this work, Duan and Curtis addressed an important issue related to the nature of working memory representations. This work is motivated by findings illustrating that orientation decoding performance for perceptual representations can be biased by the stimulus aperture (modulator). Here, the authors examined whether the decoding performance for working memory representations is similarly influenced by these aperture biases. The results provide convincing evidence that working memory representations have a different representational structure, as the decoding performance was not influenced by the type of stimulus aperture.

Strengths:

The strength of this work lies in the direct comparison of decoding performance for perceptual representations with working memory representations. The authors take well-motivated approach and illustrate that perceptual and working memory representations do not share a similar representational structure. The authors test a clear question, with a rigorous approach and provide compelling evidence. First, the presented oriented stimuli are carefully manipulated to create orthogonal biases introduced by the stimulus aperture (radial or angular modulator), regardless of the stimulus carrier orientation. Second, the authors implement advanced methods to decode the orientation information, in visual and parietal cortical regions, when directly perceiving or holding an oriented stimulus in memory. The data illustrates that working memory decoding is not influenced by the type of aperture, while this is the case in perception. In sum, the main claims are important and shed light on the nature of working memory representations.

Weaknesses:

After the authors revised the original manuscript, a few of my initial concerns remain.

(1) Theoretical framing in the introduction. The introduction proposes that decoding of orientation information during perception does not reflect orientation selectivity, and it is instead driven by coarse scale biases. This is an overstatement. Recent work shows that orientation decoding is indeed influenced by coarse biases, but also reflects orientation selectivity (Roth, Kay & Merriam, 2022).

(2) The description of the image computable V1 model remains incomplete. The steerable pyramid is a model that simulates the responses of V1 neurons. To do so, it incorporates a set of linear receptive fields with varying orientation and spatial frequency tuning. However, the information that is lacking in the Methods is whether the implemented pyramid also included two quadrature phase pairs (odd and even phase Gabor filters making the output phase invariant). The sum of the squares of the responses to these offset phase filters computes the stimulus energy within each orientation and spatial frequency channel. Without this description, it is unclear what the model output represents.
